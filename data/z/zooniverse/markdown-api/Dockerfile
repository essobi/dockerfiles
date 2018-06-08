FROM node:0.12-onbuild  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get clean  
  
WORKDIR /node_app  
  
COPY . /node_app  
  
RUN apt-get install -y supervisor  
  
RUN cd /node_app && npm install .  
  
COPY docker/supervisor.conf /etc/supervisor/conf.d/markdown_api.conf  
  
EXPOSE 2998  
ENTRYPOINT /usr/bin/supervisord  

