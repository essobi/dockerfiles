FROM titpetric/netdata  
  
RUN apt-get update && \  
apt-get install python-requests -y && \  
rm -rf /var/lib/apt/lists/* && \  
cd /root && \  
curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-latest.tgz && \  
tar -xvzf docker-latest.tgz && \  
mv /root/docker/docker /usr/bin/docker && \  
rm -r /root/docker*

