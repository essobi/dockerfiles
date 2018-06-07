FROM alpine:3.5  
ENV KOPS_VERSION=1.5.3 \  
KUBECTL_VERSION=1.6.3  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
  
VOLUME /data  
  
ADD ./resources /resources  
  
RUN /resources/build && rm -rf /resources  
  
USER kops  
  
WORKDIR /data  
  
ENTRYPOINT ["/bin/kops"]  
  
LABEL "maintainer"="cloudsquad@fxinnovation.com" \  
"org.label-schema.name"="kops" \  
"org.label-schema.base-image.name"="docker.io/library/alpine" \  
"org.label-schema.base-image.version"="3.5" \  
"org.label-schema.description"="Kops in a container" \  
"org.label-schema.url"="https://github.com/kubernetes/kops" \  
"org.label-schema.vcs-url"="https://bitbucket.org/fxadmin/public-common-
docker-kops" \  
"org.label-schema.vendor"="FXinnovation" \  
"org.label-schema.schema-version"="1.0.0-rc.1" \  
"org.label-schema.applications.kops.version"=$KOPS_VERSION \  
"org.label-schema.applications.kubectl.version"=$KUBECTL_VERSION \  
"org.label-schema.vcs-ref"=$VCS_REF \  
"org.label-schema.version"=$VERSION \  
"org.label-schema.build-date"=$BUILD_DATE \  
"org.label-schema.usage"="docker run --rm $(pwd):/data fxinnovation/kops help"  

