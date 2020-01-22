from typing import Optional, Dict, Sequence, List

import canopy


class StudyTypesCache(object):

    def __init__(
            self,
            client: canopy.swagger.ApiClient,
            authentication: canopy.Authentication,
            sim_version_cache: canopy.TenantSimVersionCache):

        self._client = client
        self._authentication = authentication
        self._sim_version_cache = sim_version_cache

        self._data: Optional[canopy.swagger.GetStudyTypesQueryResult] = None
        self._study_type_definitions_by_study_type: Optional[Dict[str, canopy.swagger.StudyTypeDefinition]] = None

    def reload(self):
        api = canopy.swagger.StudyApi(self._client)
        result: canopy.swagger.GetStudyTypesQueryResult = api.study_get_study_types()
        self._data = result

        study_types: Sequence[canopy.swagger.StudyTypeDefinition] = result.study_types
        self._study_type_definitions_by_study_type = {v.study_type.lower(): v for v in study_types}

    def get(
            self,
            sim_version: Optional[str] = None) -> canopy.swagger.GetStudyTypesQueryResult:

        if self._data is None:
            self.reload()

        if self._data is None:
            raise RuntimeError('Users for tenant ID not found.')

        if sim_version is None:
            sim_version = self._sim_version_cache.get()

        study_types_for_sim_version: List[canopy.swagger.StudyTypeDefinition] = []
        for study_type in self._data.study_types:
            study_types_for_sim_version.append(
                canopy.get_study_type_definition_for_sim_version(study_type, sim_version))

        return canopy.swagger.GetStudyTypesQueryResult(
            study_types_for_sim_version,
            self._data.sim_types,
            self._data.config_types)

    def get_study_type_definition(
            self,
            study_type: str,
            sim_version: Optional[str] = None) -> canopy.swagger.StudyTypeDefinition:

        if self._data is None:
            self.reload()

        if sim_version is None:
            sim_version = self._sim_version_cache.get()

        study_type_lower = study_type.lower()
        if study_type_lower not in self._study_type_definitions_by_study_type:
            raise canopy.NotFoundError('Study type not found: {}'.format(study_type))

        result = self._study_type_definitions_by_study_type[study_type_lower]
        return canopy.get_study_type_definition_for_sim_version(result, sim_version)

