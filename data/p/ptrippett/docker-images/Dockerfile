FROM ruby:2.5.0  
MAINTAINER paul.trippett@tuskerdirect.com  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV NGINX_VERSION 1.13.7-1~jessie  
ENV NOKOGIRI_USE_SYSTEM_LIBRARIES 1  
ENV NVM_DIR /usr/local/.nvm  
ENV NODE_VERSION stable  
  
  
##  
## Install Prerequisites  
##  
RUN apt-get update && \  
apt-get install -y --no-install-recommends libxml2 libxml2-dev libxslt1-dev
rsyslog unzip && \  
rm -rf /var/lib/apt/lists/*  
  
##  
## Install NodeJS  
##  
RUN git clone https://github.com/creationix/nvm.git $NVM_DIR && \  
cd $NVM_DIR && \  
git checkout `git describe --abbrev=0 --tags`  
RUN source $NVM_DIR/nvm.sh && \  
nvm install $NODE_VERSION && \  
nvm alias default $NODE_VERSION && \  
nvm use default  
RUN echo "source ${NVM_DIR}/nvm.sh" > $HOME/.bashrc && source $HOME/.bashrc  
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/v$NODE_VERSION/bin:$PATH  
  
##  
## Install NGINX  
##  
RUN apt-key adv --fetch-keys http://nginx.org/keys/nginx_signing.key \  
&& echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list \  
&& echo "deb http://ftp.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
nginx=${NGINX_VERSION} \  
gettext-base \  
&& rm -rf /var/lib/apt/lists/*  
ADD files/nginx.conf /etc/nginx/nginx.conf  
  
##  
## Install YARN  
##  
RUN apt-key adv --fetch-keys https://dl.yarnpkg.com/debian/pubkey.gpg \  
&& echo "deb http://dl.yarnpkg.com/debian/ stable main" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y yarn \  
&& rm -rf /var/lib/apt/lists/*  
  
##  
## Configure rsyslogd  
##  
ADD files/rsyslog.conf /etc/rsyslog.conf  
ADD files/rsyslog.sh /rsyslog.sh  
  
##  
## Configure envconsul  
##  
ENV ENVCONSUL_VERSION 0.7.3  
RUN cd /tmp \  
&& wget
https://releases.hashicorp.com/envconsul/${ENVCONSUL_VERSION}/envconsul_${ENVCONSUL_VERSION}_linux_amd64.zip
\  
&& unzip envconsul_${ENVCONSUL_VERSION}_linux_amd64.zip \  
&& mv envconsul /usr/local/bin/envconsul \  
&& rm envconsul_${ENVCONSUL_VERSION}_linux_amd64.zip  
  
##  
## Setup Start command  
##  
RUN chmod 755 /rsyslog.sh  

