FROM busybox  
  
EXPOSE 53  
CMD ["/mesos-dns"]  
  
ADD https://github.com/mesosphere/mesos-dns/releases/download/v0.5.2/mesos-
dns-v0.5.2-linux-amd64 /mesos-dns  
  
RUN chmod 755 /mesos-dns  

