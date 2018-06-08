FROM ubuntu:trusty  
MAINTAINER Alpha Hinex <AlphaHinex@gmail.com>  
  
RUN apt-get update && apt-get -y install httrack python  
  
ENV BASE /usr/local  
ENV WEB_BASE $BASE/websites/material-design-docs  
  
WORKDIR $BASE  
RUN httrack https://www.google.com/design/spec/ -O $WEB_BASE  
  
WORKDIR $WEB_BASE  
EXPOSE 80  
CMD python -m SimpleHTTPServer 80  

