FROM node:8.0.0-alpine  
  
MAINTAINER Konstantin Grachev <me@grachevko.ru>  
  
ENV STANDARDJS_VERSION 10.0.2  
RUN echo "standard@${STANDARDJS_VERSION}"  
RUN npm install -g "standard@${STANDARDJS_VERSION}"  
  
ENTRYPOINT ["standard"]  
CMD ["--help"]  

