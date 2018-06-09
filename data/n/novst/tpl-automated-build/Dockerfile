FROM openjdk:jdk-alpine  
  
ARG BUILD_DATE  
  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://github.com/nWmCZ/TPL.git" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="1.0.0-rc.1"  
  
ENV TIMEOUT=0  
EXPOSE 8080  
COPY . /  
  
RUN ./gradlew clean build  
  
ENTRYPOINT ["sh", "-c", "sleep ${TIMEOUT} && java -jar ./build/libs/*.jar
--spring.config.location=/tpl/"]  

