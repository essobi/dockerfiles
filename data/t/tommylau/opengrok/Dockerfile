FROM ubuntu:16.04  
MAINTAINER Tommy Lau <tommy@gen-new.com>  
  
# Setup useful environment variables  
ENV GROK_HOME /grok  
ENV OPENGROK_INSTANCE_BASE ${GROK_HOME}  
ENV GROK_VERSION 0.12.1.6  
#ENV DOWNLOAD_URL
https://github.com/OpenGrok/OpenGrok/files/467358/opengrok-${GROK_VERSION}.tar.gz.zip  
ENV DEBIAN_FRONTEND noninteractive  
  
LABEL Description="This image is used to start OpenGrok" Vendor="Tommy Lau"
Version="${GROK_VERSION}"  
  
# Install needed packages  
RUN apt update -qq \  
&& apt install -y --no-install-recommends exuberant-ctags git inotify-tools
openjdk-8-jdk-headless tomcat7 unzip wget \  
&& apt clean autoclean \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
# Get stable version  
RUN set -x \  
&& mkdir /opengrok \  
&& cd /usr/src \  
&& DOWNLOAD_URL=`wget -qO-
"https://github.com/OpenGrok/OpenGrok/releases/${GROK_VERSION}" | sed -n
's/.*\\(https.*.gz.zip\\)\".*/\1/p'` \  
&& wget -c "${DOWNLOAD_URL}" \  
&& unzip opengrok-*.zip \  
&& tar zxvf opengrok-*.tar.gz -C /opengrok --strip-components=1 \  
&& /opengrok/bin/OpenGrok deploy \  
&& rm -fr opengrok-*  
  
ADD run.sh /rungrok  
  
ENTRYPOINT ["/rungrok"]  
  
EXPOSE 8080  

