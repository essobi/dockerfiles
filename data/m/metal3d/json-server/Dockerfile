FROM node:latest  
MAINTAINER Patrice FERLET <metal3d@gmail.com>  
  
EXPOSE 3000  
# to be able to use --user, node need to write  
# data to $HOME, but using root will break that possibility, so  
# use /project instead  
ENV HOME /project  
WORKDIR /project  
  
ADD entrypoint.sh /entrypoint.sh  
  
RUN set -ex; \  
chmod +x /entrypoint.sh; \  
chmod a+w /project; \  
npm install -g json-server;  
RUN set -xe; \  
groupadd -g 1001 jsonserver; \  
useradd -u 1001 -g 1001 -m jsonserver; \  
chown -R jsonserver:jsonserver /project  
  
USER 1001  
ENTRYPOINT ["/entrypoint.sh"]  

