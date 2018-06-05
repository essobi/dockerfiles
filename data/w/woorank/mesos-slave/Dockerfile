FROM mesosphere/mesos-slave:0.25.0-0.2.70.ubuntu1404  
  
RUN apt-get update && \  
apt-get install -y curl && \  
curl -fLsS https://get.docker.com/ | sh && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  

