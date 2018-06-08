FROM openjdk:8  
ENV WORKER_HOME /opt/pubsub-worker  
  
RUN mkdir -p /opt/app  
  
COPY . /opt/app  
WORKDIR /opt/app  
  
ENTRYPOINT /opt/app/docker/startup.sh  

