FROM ubuntu:14.04  
MAINTAINER didstopia  
  
# Add the Docker repository  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D  
RUN echo deb http://apt.dockerproject.org/repo ubuntu-trusty main >
/etc/apt/sources.list.d/docker.list  
  
# Run a quick apt-get update/upgrade  
RUN apt-get update && apt-get upgrade -y && apt-get autoremove -y --purge  
  
# Install both Docker and Docker Cloud (and additional dependencies)  
RUN apt-get install -y docker-engine python-pip git-core  
RUN pip install --upgrade pip  
RUN pip install docker-cloud  
  
# Setup some Docker inside Docker magic  
ADD wrapdocker /usr/local/bin/wrapdocker  
RUN chmod +x /usr/local/bin/wrapdocker  
  
# Setup default environment variables  
ENV DOCKER_LOGIN ""  
ENV DOCKER_PASSWORD ""  
ENV DOCKER_EMAIL ""  
# Set the entrypoint  
ENTRYPOINT ["/bin/bash"]

