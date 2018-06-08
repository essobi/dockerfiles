FROM mobingi/ubuntu-nginx-base  
  
ENV NAVE_DIR /opt/nave  
RUN /provision.sh && rm -f /provision.sh  
ADD startup.sh /startup.sh  
  
EXPOSE 22 80  
ENTRYPOINT ["/run.sh"]  

