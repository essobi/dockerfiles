FROM openjdk:8u131-jdk-alpine  
LABEL maintainer="Gary A. Stafford <garystafford@rochester.rr.com>"  
ENV REFRESHED_AT 2017-11-21  
VOLUME /tmp  
EXPOSE 8080  
RUN set -ex \  
&& apk update \  
&& apk upgrade \  
&& apk add git  
RUN mkdir /election \  
&& git clone \--depth 1 --branch build-artifacts \  
"https://github.com/garystafford/election-service.git" /election \  
&& cd /election \  
&& mv election-service-*.jar election-service.jar  
CMD [ "java", "-Djava.security.egd=file:/dev/./urandom", "-jar",
"election/election-service.jar" ]  

