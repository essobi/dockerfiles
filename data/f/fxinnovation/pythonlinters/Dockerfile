FROM alpine:3.7  
VOLUME /data  
  
ENV PYTHON3_VERSION=3.6.3-r9 \  
PYLINT_VERSION=1.8.4 \  
MYPY_VERSION=0.600  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
  
ADD ./resources /resources  
  
RUN /resources/build && rm -rf /resources  
  
WORKDIR /data  
  
LABEL "maintainer"="cloudsquad@fxinnovation.com" \  
"org.label-schema.name"="pythonlinters" \  
"org.label-schema.base-image.name"="docker.io/library/alpine" \  
"org.label-schema.base-image.version"="3.7" \  
"org.label-schema.description"="python linters in a container" \  
"org.label-schema.url"="https://bitbucket.org/fxadmin/public-common-docker-
pythonlinters" \  
"org.label-schema.vcs-url"="https://bitbucket.org/fxadmin/public-common-
docker-pythonlinters" \  
"org.label-schema.vendor"="FXinnovation" \  
"org.label-schema.schema-version"="1.0.0-rc.1" \  
"org.label-schema.applications.pylint.version"=$PYLINT_VERSION \  
"org.label-schema.applications.python3.version"=$PYTHON3_VERSION \  
"org.label-schema.applications.mypy.version"=$MYPY_VERSION \  
"org.label-schema.vcs-ref"=$VCS_REF \  
"org.label-schema.version"=$VERSION \  
"org.label-schema.build-date"=$BUILD_DATE \  
"org.label-schema.usage"="docker run --rm -v $(pwd):/data
fxinnovation/pythonlinters [PYTHONLINTERS_COMPONENT] [COMMAND_OPTIONS]"  

