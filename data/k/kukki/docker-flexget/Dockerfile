FROM alpine  
MAINTAINER Jimmy Koo <kukkiz@gmail.com  
ARG BUILD_DATE  
ARG VCS_REF  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.license="GPL v3" \  
org.label-schema.name="Docker FlexGet" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-type="Git" \  
org.label-schema.vcs-url="https://bitbucket.org/jkoo/docker-flexget"  
  
RUN apk add --update \  
python \  
py-pip \  
ca-certificates  
  
RUN pip install paver  
RUN pip install flexget  
RUN pip install transmissionrpc  
RUN mkdir /root/.flexget  
  
WORKDIR /opt/flexget  
  
VOLUME ["/root/.flexget"]  
  
ENTRYPOINT ["flexget"]  

