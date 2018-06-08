FROM tobilg/mesos:0.24.0  
MAINTAINER tobilg <fb.tools.github@gmail.com>  
  
# Mesos fetcher uses unzip to extract staged zip files  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND="noninteractive" \  
apt-get install -yq --no-install-recommends --force-yes unzip && \  
rm -rf /var/lib/apt/lists/*  
  
RUN wget -O - https://get.docker.com/ | sh  
  
EXPOSE 5051  
CMD ["mesos-slave"]

