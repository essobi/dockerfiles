FROM python:2.7  
MAINTAINER Kazuya Yokogawa "yokogawa-k@klab.com"  
RUN pip install grip  
COPY entrypoint.sh /entrypoint.sh  
  
WORKDIR /work  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["--help"]  

