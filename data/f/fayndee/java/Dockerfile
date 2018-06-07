FROM dockerfile/java:oracle-java8  
MAINTAINER Fang Yuan <fayndee@hotmail.com>  
  
# Expose the docker container name as an environment variable  
RUN echo 'export DOCKER_CONTAINER_NAME=$(curl -s $(netstat -nr | grep
'"'"'^0\\.0\\.0\\.0'"'"' | awk '"'"'{print
$2}'"'"'):2375/containers/$(hostname)/json | sed -nr
'"'"'s/.*?"Name":"\/(\w+)".*/\\\1/p'"'"')' >> ~/.bashrc  

