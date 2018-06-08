FROM phusion/baseimage  
MAINTAINER Daniel Haus <daniel.haus@businesstools.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get install -yq \  
nodejs npm nginx  
  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN mkdir -p /usr/app && cp -a /tmp/node_modules /usr/app/  
  
ADD package.json /usr/app/package.json  
ADD .babelrc /usr/app/.babelrc  
  
ADD etc/default.conf /etc/nginx/sites-available/default  
  
RUN mkdir /etc/service/nginx  
ADD etc/nginx.run.sh /etc/service/nginx/run  
  
RUN mkdir /etc/service/npm  
ADD etc/npm.run.sh /etc/service/npm/run  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80  
WORKDIR /usr/app/  
  
ONBUILD ADD package.json /usr/app/  
ONBUILD RUN npm install  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

