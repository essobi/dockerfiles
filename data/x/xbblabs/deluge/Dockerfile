FROM ubuntu:18.04  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends apt-utils gnupg \  
&& echo "deb http://ppa.launchpad.net/deluge-team/ppa/ubuntu bionic main" >>
/etc/apt/sources.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
8EED8FB4A8E6DA6DFDF0192BC5E6A5ED249AD24C \  
&& apt-get update \  
&& apt-get dist-upgrade -y \  
&& apt-get install -y --no-install-recommends deluged deluge-console deluge-
web gosu net-tools \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV TINI_VERSION v0.18.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/sbin/tini  
RUN chmod +x /sbin/tini  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod 700 /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 58846/tcp 8112/tcp  
  
LABEL maintainer="nicola@xbblabs.com"  

