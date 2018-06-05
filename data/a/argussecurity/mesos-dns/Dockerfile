FROM busybox  
  
WORKDIR /app  
EXPOSE 53 8123  
ENTRYPOINT ["/bin/sh", "./mesos-dns.sh"]  
  
ADD app/ /app  
ADD https://github.com/mesosphere/mesos-dns/releases/download/v0.5.2/mesos-
dns-v0.5.2-linux-amd64 ./mesos-dns  
  
RUN chmod +x ./mesos-dns  

