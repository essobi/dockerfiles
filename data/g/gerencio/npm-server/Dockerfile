FROM gerencio/alpine-env:node-6.9.1  
MAINTAINER Clayton Silva <clayton@xdevel.com.br>  
WORKDIR /opt/sinopia  
  
RUN apk add --update \  
python \  
python-dev \  
py-pip \  
build-base \  
&& pip install virtualenv \  
&& rm -rf /var/cache/apk/*  
  
RUN npm -g install js-yaml sinopia2 sinopia-github-oauth  
RUN mkdir config  
ADD config.yaml /tmp/config.yaml  
ADD start.sh /opt/sinopia/start.sh  
CMD ["sh","/opt/sinopia/start.sh"]  
EXPOSE 4873  
VOLUME /opt/sinopia  

