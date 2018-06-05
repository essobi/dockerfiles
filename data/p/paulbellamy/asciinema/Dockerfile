FROM debian:jessie  
  
RUN apt-get update  
RUN apt-get install -y asciinema  
ENV SHELL /bin/bash  
ENV USER root  
  
ENTRYPOINT ["asciinema", "rec"]  

