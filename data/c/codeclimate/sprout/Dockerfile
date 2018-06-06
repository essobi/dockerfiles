FROM codeclimate/alpine-ruby:b38  
  
# Using wget errors getting the docker executable:  
#  
# Connecting to get.docker.com (...)  
# wget: error getting response: Connection reset by peer  
#  
# cURL works though.  
RUN apk --update add curl  
  
ENV DOCKER_VERSION=1.10.3  
ENV
DOCKER_URL=https://get.docker.com/builds/Linux/x86_64/docker-$DOCKER_VERSION  
RUN curl -o /bin/docker $DOCKER_URL && chmod +x /bin/docker  
  
COPY . /usr/src/app  
WORKDIR /usr/src/app  
ENTRYPOINT ["bin/sprout"]  

