FROM openapitools/openapi-generator-cli
ENV PATH="/opt/openapi-generator/modules/openapi-generator-cli/target:${PATH}"
RUN mkdir /canopy
RUN ln -s /opt/openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar /canopy/openapi-generator-cli.jar
WORKDIR /canopy
