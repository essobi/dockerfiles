FROM python:2.7  
RUN pip install locustio pyzmq  
  
ADD run.sh /usr/local/bin/run.sh  
RUN chmod 755 /usr/local/bin/run.sh  
  
EXPOSE 8089 5557 5558  
CMD ["/usr/local/bin/run.sh"]  

