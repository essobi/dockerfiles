FROM node:7.4.0-alpine  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Docker DocToc" \  
org.label-schema.description="Generates table of contents for markdown files
inside local git repository." \  
org.label-schema.url="http://andradaprieto.es" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/jandradap/doctoc" \  
org.label-schema.vendor="Jorge Andrada Prieto" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0" \  
maintainer="Jorge Andrada Prieto <jandradap@gmail.com>" \  
org.label-schema.docker.cmd="docker run --rm -it -v $(pwd):/usr/src
jorgeandrada/doctoc --gitlab"  
  
RUN npm install -g doctoc && \  
mkdir /usr/src  
  
WORKDIR /usr/src  
  
ENTRYPOINT ["doctoc", ".", "--notitle"]  

