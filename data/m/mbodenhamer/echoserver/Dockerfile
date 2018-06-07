FROM mbodenhamer/alpine-flask:latest  
MAINTAINER Matt Bodenhamer <mbodenhamer@mbodenhamer.com>  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
COPY serve.py /serve.py  
  
WORKDIR /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

