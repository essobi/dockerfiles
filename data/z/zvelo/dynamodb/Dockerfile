FROM node:alpine  
MAINTAINER Joshua Rubin <jrubin@zvelo.com>  
  
RUN npm install -g dynalite  
  
EXPOSE 8001  
ENTRYPOINT ["dynalite"]  
CMD ["--ssl", "false", "--port", "8001"]  

