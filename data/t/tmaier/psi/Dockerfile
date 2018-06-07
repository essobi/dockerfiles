FROM node:7-alpine  
MAINTAINER Tobias L. Maier <tobias.maier@baucloud.com>  
  
RUN npm install --save -g psi  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["--help"]  

