FROM openjdk:8-jre-alpine  
  
ARG VALIDATOR_RELEASE_VERSION=18.3.0  
ENV VALIDATOR_FILE vnu.jar_${VALIDATOR_RELEASE_VERSION}.zip  
ENV VALIDATOR_ZIP
https://github.com/validator/validator/releases/download/${VALIDATOR_RELEASE_VERSION}/vnu.jar_${VALIDATOR_RELEASE_VERSION}.zip  
  
RUN apk add --no-cache --virtual .build-deps unzip wget \  
&& wget -q ${VALIDATOR_ZIP} \  
&& unzip -q ${VALIDATOR_FILE} \  
&& mv dist/vnu.jar / \  
&& rm -rf dist \  
&& apk del .build-deps  
  
RUN echo -e '#!/bin/ash\njava -jar /vnu.jar $@' > /usr/bin/validator && \  
chmod +x /usr/bin/validator  
  
EXPOSE 8888  
CMD ["java", "-cp", "/vnu.jar", "nu.validator.servlet.Main", "8888"]  

