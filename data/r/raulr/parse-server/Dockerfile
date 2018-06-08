FROM node:argon  
MAINTAINER Raul Rodriguez <raul@raulr.net>  
  
ENV PARSE_SERVER_VERSION 2.2.24  
RUN npm install -g parse-server@${PARSE_SERVER_VERSION}  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
EXPOSE 1337  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["parse-server"]

