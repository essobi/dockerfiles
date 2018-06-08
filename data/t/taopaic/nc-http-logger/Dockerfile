FROM busybox  
MAINTAINER TaopaiC <pctao.tw@gmail.com>  
  
WORKDIR /app/  
ADD logger.sh index.html ./  
  
EXPOSE 80 9080 9000 8080  
ENV PORT=80  
CMD /app/logger.sh

