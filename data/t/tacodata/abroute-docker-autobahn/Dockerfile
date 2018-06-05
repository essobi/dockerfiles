FROM tacodata/abroute-docker-base  
#  
# this runs the autobahn router for authentication and authorization  
# it expects a database to be up and running, details  
# about it are in the abenv file  
#  
MAINTAINER Greg Fausak <greg@tacodata.com>  
  
COPY abrouter /usr/local/bin/  
  
EXPOSE 18080  
ENTRYPOINT ["abrouter"]  

