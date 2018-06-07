FROM huksley/ubuntu-dind  
  
#install soft  
RUN apt-get update  
RUN apt-get install -y curl python-pip openjdk-8-jdk git sed maven  
RUN export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64/  
RUN pip install docker-compose  
RUN export DOCKER_CLIENT_TIMEOUT=120  
RUN export COMPOSE_HTTP_TIMEOUT=120  
RUN export SASS_FORCE_BUILD=1  
  
  

