FROM anapsix/alpine-java  
  
ENV JSON_SCHEMA_VALIDATOR_VERSION 2.2.8  
ENV LANG en_US.UTF-8  
RUN apk add --no-cache curl \  
&& mkdir /app \  
&& curl -L https://repo1.maven.org/maven2/com/github/java-json-tools/json-
schema-validator/${JSON_SCHEMA_VALIDATOR_VERSION}/json-schema-
validator-${JSON_SCHEMA_VALIDATOR_VERSION}-lib.jar -o /app/json-schema-
validator.jar \  
&& apk del curl  
  
ENTRYPOINT [ "java", "-classpath", "/app/json-schema-validator.jar",
"com.github.fge.jsonschema.main.cli.Main" ]  
CMD [ "--help" ]  

