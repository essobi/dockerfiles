FROM capside/nodejs:v4.1.0  
MAINTAINER Javi Moreno <javi.moreno@capside.com>  
  
  
RUN wget https://raw.githubusercontent.com/lsabin/docker-intro-
demo/master/webservice.js \  
\--no-check-certificate  
  
#A linked container could access to this port  
EXPOSE 8888  
CMD ["/node/bin/node", "webservice.js"]  
  

