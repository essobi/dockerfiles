FROM alpine:3.5  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL maintainer="axeclbr@posteo.de" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="axeclbr/docker-git" \  
org.label-schema.description="Docker-Container behaving (nearly) like a git-
binary" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/axeclbr/docker-git" \  
org.label-schema.vendor="axeclbr" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
RUN apk --update add git \  
&& rm -rf /var/cache/apk/*  
  
ENV HOME /root  
  
# Put convienience-script into container to have it accessible  
# without checking out from github-repo. Display with:  
# $ docker run --entrypoint=/bin/cat axeclbr/git /root/git  
COPY git /root/git  
VOLUME /root/workspace  
WORKDIR /root/workspace  
  
ENTRYPOINT ["/usr/bin/git"]  
  

