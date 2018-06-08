FROM node:5  
MAINTAINER Kazumichi Yamamoto <yamamoto.febc@gmail.com>  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["--help"]  
  
RUN npm install -g sacloud  
RUN sacloud --install >> /root/.bashrc  

