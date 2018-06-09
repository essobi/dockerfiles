# Dockerfile for installing and running Nginx  
# Select ubuntu as the base image  
FROM ubuntu  
MAINTAINER M Bintang <halilintar8@yahoo.com>  
  
VOLUME ["/certs"]  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
#Set Environment Variable  
ENV NODE_ENV production  
ENV NODE_CONFIG_DIR /src/config  
  
# Install Required Packages  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get -y install curl unzip git wget vim nginx python-setuptools
libkrb5-dev build-essential  
#RUN curl -sL https://deb.nodesource.com/setup_0.10 | bash -  
#RUN apt-get install -y nodejs  
#RUN apt-get install -y npm  
#RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN export TERM=xterm  
  
# Setup Nginx  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/"
/etc/nginx/nginx.conf  
RUN sed -i -e"s/keepalive_timeout 2/keepalive_timeout
2;\n\tclient_max_body_size 100m/" /etc/nginx/nginx.conf  
RUN sed -i -e"s/# server_tokens off;/server_tokens off;/"
/etc/nginx/nginx.conf  
ADD /config/default.conf /etc/nginx/sites-available/default  
  
# Setup NodeJS Application  
RUN useradd -M node  
ADD /src /src  
RUN chown -R node:node /src  
  
WORKDIR /src  
RUN wget nodejs.org/dist/v0.10.45/node-v0.10.45-linux-x64.tar.gz  
RUN tar -C /usr/local \--strip-components 1 -xzf
node-v0.10.45-linux-x64.tar.gz  
RUN ln -s /usr/local/bin/node /usr/bin/node  
RUN ln -s /usr/local/bin/npm /usr/bin/npm  
RUN npm -g update npm  
RUN npm install  
  
# Run Supervisord  
RUN /usr/bin/easy_install supervisor  
RUN /usr/bin/easy_install supervisor-stdout  
RUN /usr/bin/easy_install superlance  
ADD /config/supervisord.conf /etc/supervisord.conf  
  
# Publish port  
EXPOSE 443  
CMD ["/usr/local/bin/supervisord","-n"]  

