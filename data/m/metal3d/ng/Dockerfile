FROM node:latest  
MAINTAINER Patrice Ferlet <metal3d@gmail.com>  
  
WORKDIR /project  
EXPOSE 4200 49152  
ENV HOME /tmp  
  
RUN set -ex; \  
npm install -g angular-cli; \  
npm cache clean;  
  
ENTRYPOINT ["ng"]  
CMD ["--help"]  

