FROM dockerfile/ansible  
MAINTAINER SequenceIQ  
  
RUN pip install boto  
RUN pip install awscli  
RUN pip install apache-libcloud  
  
COPY init.sh /  
RUN chmod +x /init.sh  
  
ENTRYPOINT ["/init.sh"]  

