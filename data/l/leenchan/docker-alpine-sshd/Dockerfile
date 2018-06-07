FROM alpine:edge  
  
MAINTAINER leenchan  
  
ADD conf /conf  
ADD run /run  
ADD docker.sh /tmp/docker.sh  
RUN chmod +x /tmp/docker.sh && /tmp/docker.sh && rm -f /tmp/docker.sh  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
EXPOSE 80 22  
CMD ["/run.sh"]  

