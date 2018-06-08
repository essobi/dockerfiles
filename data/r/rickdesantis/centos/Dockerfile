FROM centos:6.7  
MAINTAINER Riccardo B. Desantis <riccardobenito.desantis@gmail.com>  
  
# Setting the environment  
ENV HOSTNAME centos.rickdesantis.docker.com  
ENV USERHOME /root  
ENV USER root  
  
WORKDIR $USERHOME  
# Update the repos and install all the used packages  
RUN yum update -y -q && \  
touch /tmp/empty  
  
# Fake command  
CMD tail -F /tmp/empty  
  
# Build: docker build -t centos1 ../centos  
# Run: docker run --name=centos1 centos1 &  
# Bash: docker exec -it centos1 bash  
# Start: docker start centos1  
# Stop: docker stop centos1  

