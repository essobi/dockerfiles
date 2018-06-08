FROM ubuntu:16.04  
MAINTAINER chi@softpro.de  
  
RUN apt-get update && apt-get install -y -q vim unzip wget curl openjdk-8-jre-
headless  
  
ENV FROM_OS=ubuntu  
  
RUN echo 'alias ll="ls -lA --color"' >> /etc/bash.bashrc  
  
COPY start.sh /  
  
ENTRYPOINT ["/start.sh"]  
CMD ["bash"]  

