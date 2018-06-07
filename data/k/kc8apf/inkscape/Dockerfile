FROM kc8apf/x11-app-base  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION=0.92.2\\*  
  
LABEL org.label-schema.name="Inkscape" \  
org.label-schema.description="Professional vector graphics editor" \  
org.label-schema.usage="https://github.com/kc8apf/docker-
inkscape/blob/$VERSION/README.md" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/kc8apf/docker-inkscape" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
RUN apt-get install -y software-properties-common && \  
apt-add-repository ppa:inkscape.dev/stable && \  
apt-get update && \  
apt-get install -y inkscape=$VERSION  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh", "-p", "inkscape"]  

