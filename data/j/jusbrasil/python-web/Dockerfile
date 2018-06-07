FROM python:2.7.8  
# Set versions as environment variables so that they can be inspected later.  
ENV LESSC_VERSION=1.7.5 \  
LIBSASS_VERSION=3.11.2  
# Update the package repository  
RUN set -x; \  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
wget \  
curl \  
nodejs \  
npm \  
libssl-dev \  
ruby \  
locales  
  
# Configure timezone and locale  
RUN echo "America/Sao_Paulo" > /etc/timezone; dpkg-reconfigure -f
noninteractive tzdata  
RUN echo 'pt_BR.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen &&
DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales  
  
# Install Nginx  
RUN apt-get install -y nginx  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# Replace the default path for VCS dependencies  
ENV PIP_SRC /usr/local/src  
# Upgrade pip and install Python packages  
RUN pip install -U pip && pip install nose pytest mock gunicorn  
  
# Install node packages  
RUN ln -s /usr/bin/nodejs /usr/bin/node \  
&& npm install -g bower \  
&& npm install -g grunt-cli \  
&& npm install -g phantomjs  
  
# Install CSS processors  
RUN npm install -g \  
less@${LESSC_VERSION} \  
node-sass@${LIBSASS_VERSION}  
  
# Based on python onbuild images  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  

