FROM logstash:2.2  
MAINTAINER Marcus Hughes <hello@msh100.uk>  
  
WORKDIR /config/  
  
ADD logstash.template init.sh patterns/s3 /config/  
RUN mkdir patterns/ && \  
mv s3 patterns/ && \  
chmod +x init.sh  
  
CMD ["/config/init.sh"]  

