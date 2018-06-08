FROM docker  
MAINTAINER Neoskop DevOps <devops@neoskop.de>  
  
RUN apk add mysql-client netcat-openbsd jq --no-cache  
COPY run.sh /usr/local/bin/  
CMD ["/usr/local/bin/run.sh"]  

