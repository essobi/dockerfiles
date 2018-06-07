###############################################################  
# Historic API support for the Rolltime family of applications.  
# Receives links from a PostgreSQL container (as postgres).  
###############################################################  
  
FROM node:latest  
  
RUN \  
git clone https://github.com/rolltime/rolltime-historic-api \  
&& cd rolltime-historic-api \  
&& make setup  
  
WORKDIR "/rolltime-historic-api"  
  
CMD ["make", "run"]  
  
EXPOSE 2000  

