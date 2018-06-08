FROM shouldbee/flyway  
  
MAINTAINER Gokhan Sengun <gokhansengun@gmail.com>  
  
RUN apt-get update && apt-get -y install postgresql-client curl jq  
  
COPY run-flyway.sh /scripts/run-flyway.sh  
  
# only a hack, will be fixed in later version of docker-compose  
RUN chmod +x /scripts/run-flyway.sh  
  
WORKDIR /flyway  
  
ENTRYPOINT [ "/scripts/run-flyway.sh" ]  

