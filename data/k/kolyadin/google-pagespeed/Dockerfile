FROM node:7-alpine  
  
MAINTAINER aleksey.kolyadin@isobar.ru  
  
RUN npm install --save -g psi  
  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["--help"]

