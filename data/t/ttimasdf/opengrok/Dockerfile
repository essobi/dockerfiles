FROM tomcat  
MAINTAINER Tim Zhang "https://github.com/ttimasdf"  
ENV DEBIAN_FRONTEND=noninteractive OPENGROK_INSTANCE_BASE=/grok
OPENGROK_TOMCAT_BASE=${CATALINA_HOME}  
ARG CI=false  
  
ADD install.sh /usr/local/bin/install  
ADD run.sh /usr/local/bin/run  
ADD loc.sh /usr/local/bin/loc  
RUN CI=$CI loc -u && \  
apt-get update && \  
apt-get install -y \  
exuberant-ctags \  
git \  
subversion \  
mercurial \  
wget \  
zip \  
inotify-tools && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/usr/local/bin/run"]  
  
EXPOSE 8080  
RUN /usr/local/bin/install  
  
# Build-time metadata as defined at http://label-schema.org  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="OpenGrok" \  
org.label-schema.description="The one-liner to spin up a code search engine,
stays latest" \  
org.label-schema.url="https://github.com/ttimasdf/docker-opengrok" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/ttimasdf/docker-opengrok" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  

