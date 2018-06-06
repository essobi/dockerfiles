FROM debian:latest  
  
MAINTAINER DroneDeploy <dev@dronedeploy.com>  
LABEL Description="Sensu Client docker image" Vendor="DroneDeploy"
Version="0.1.0"  
  
ENV PATH /opt/sensu/embedded/bin:$PATH  
ENV LOG_LEVEL debug  
ENV CONFIG_FILE /etc/sensu/config.json  
ENV CONFIG_DIR /etc/sensu/conf.d  
ENV CLIENT_SUBSCRIPTIONS all,default  
ENV HOST_DEV_DIR /dev  
ENV HOST_PROC_DIR /proc  
ENV HOST_SYS_DIR /sys  
ENV CERT_SECRET false  
  
RUN apt-get update && apt-get install -y wget ca-certificates && apt-get -y
clean && \  
wget -q http://repositories.sensuapp.org/apt/pubkey.gpg -O- | apt-key add - &&
\  
echo "deb http://repositories.sensuapp.org/apt sensu main" | tee
/etc/apt/sources.list.d/sensu.list  
  
RUN apt-get update && \  
apt-get install -y sensu ruby-dev build-essential bc && \  
apt-get -y clean && \  
wget https://github.com/jwilder/dockerize/releases/download/v0.0.2/dockerize-
linux-amd64-v0.0.2.tar.gz && \  
tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.0.2.tar.gz  
  
COPY sensu_client_key.pem /etc/sensu/ssl/sensu_client_key.pem  
COPY sensu_client_cert.pem /etc/sensu/ssl/sensu_client_cert.pem  
COPY start /bin/start  
ADD templates /etc/sensu/templates  
  
RUN /opt/sensu/embedded/bin/gem install sensu-plugins-io-checks sensu-plugins-
process-checks sensu-plugins-load-checks sensu-plugins-cpu-checks sensu-
plugins-disk-checks sensu-plugins-memory-checks  
  
ENTRYPOINT ["/bin/start"]  

