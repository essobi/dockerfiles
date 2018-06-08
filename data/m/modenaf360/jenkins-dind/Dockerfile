FROM jenkins:latest  
USER root  
RUN apt-get update && apt-get -y install vim git wget maven  
RUN wget https://get.docker.com/builds/Linux/x86_64/docker-17.05.0-ce.tgz  
  
RUN tar xvfz docker-17.05.0-ce.tgz  
  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN cp ./docker/docker /usr/bin/  
  
ENV JAVA_ARGS -Xms512m -Xmx1024m  
  
ADD bootstrap.sh /bootstrap.sh  
  
RUN chmod +x /bootstrap.sh  
  
CMD ["/bootstrap.sh"]  
  

