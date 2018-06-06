FROM cbrake/oe-build  
MAINTAINER Seppe Stas <seppe@productize.be>  
  
USER root  
RUN apt-get update -qq && apt-get install -yq curl jq && rm -rf
/var/lib/apt/lists/*  
  
USER build  

