FROM python:2.7  
RUN pip install -I flexget transmissionrpc  
  
RUN mkdir -p /root/.flexget  
  
ADD config.yaml /root/.flexget/config.yml  
  
VOLUME ["/root/.flexget"]  
  
EXPOSE 5050  
CMD ["/usr/local/bin/flexget", "--loglevel", "info", "daemon", "start"]  

