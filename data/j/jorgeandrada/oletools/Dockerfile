FROM python:2.7-alpine  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="oletools" \  
org.label-schema.description="oletools - python tools to analyze MS OLE2 files
(Structured Storage, Compound File Binary Format) and MS Office documents, for
malware analysis, forensics and debugging." \  
org.label-schema.url="http://andradaprieto.es" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/jandradap/oletools" \  
org.label-schema.vendor="Jorge Andrada Prieto" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0" \  
maintainer="Jorge Andrada Prieto <jandradap@gmail.com>" \  
org.label-schema.docker.cmd="docker run --rm -it --name oletools -v
$(pwd):/srv jorgeandrada/oletools:latest sh"  
  
RUN pip install -U oletools  
  
WORKDIR /srv  

