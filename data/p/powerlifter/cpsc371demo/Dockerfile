FROM ubuntu:16.04  
MAINTAINER Warren Marusiak marusiak@unbc.ca  
  
WORKDIR /  
  
RUN apt-get update  
  
COPY doit /  
  
RUN useradd foo  
  
RUN chown foo doit  
  
RUN chmod +x doit  
  
USER foo  
  
ENTRYPOINT ["/doit"]  
  
CMD ["this", "is", "default", "parameters"]  

