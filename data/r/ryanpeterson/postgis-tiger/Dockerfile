FROM ryanpeterson/postgis  
MAINTAINER Ryan Peterson <ryan.m.peterson@gmail.com>  
  
ENV TIGER_COUNTRY_SCRIPT /tmp/tiger-country.sh  
ENV TIGER_STATE_SCRIPT /tmp/tiger-state.sh  
  
# loads New York state TIGER data by default  
ENV TIGER_STATES NY  
  
ADD init/ docker-entrypoint-initdb.d/  
  

