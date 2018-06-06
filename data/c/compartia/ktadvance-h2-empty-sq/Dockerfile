FROM sonarqube:5.6.4-alpine  
ARG CACHE_TAG  
ENV FROM_VERSION=${CACHE_TAG}  
  
MAINTAINER Artem Zaborskiy “artem@toptal.com"  
  
RUN apk --no-cache add --repository http://dl-
cdn.alpinelinux.org/alpine/edge/community wget ca-certificates  
  
ENV PLUGINS_DIR /opt/sonarqube/extensions/plugins  
  
WORKDIR $PLUGINS_DIR  
RUN wget https://github.com/kestreltechnology/sonar-kt-
advance/releases/download/$FROM_VERSION/sonar-kt-advance-
plugin-$FROM_VERSION.jar  
RUN ls -la $PLUGINS_DIR  
WORKDIR $SONARQUBE_HOME  

