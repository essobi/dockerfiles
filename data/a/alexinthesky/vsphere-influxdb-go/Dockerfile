FROM debian:stable-slim  
ENV VERSION="0.8.4"  
ADD https://github.com/Oxalide/vsphere-influxdb-
go/releases/download/v0.8.4/vsphere-influxdb-go_${VERSION}_linux_amd64.deb /  
RUN dpkg -i /vsphere-influxdb-go*.deb  
ENV INTERVAL_IN_SECONDS=300  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

