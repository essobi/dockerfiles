FROM ubuntu:xenial  
  
# Add certbot ppa  
RUN apt-get update && apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:certbot/certbot  
  
# Instal mosquitto and certbot  
RUN apt-get update && apt-get install -y \  
mosquitto \  
mosquitto-clients \  
certbot \  
cron  
  
ENTRYPOINT ["/init"]  
EXPOSE 8883 9001  
VOLUME /mosquitto /etc/letsencrypt  
  
# Install services  
COPY services /etc/services.d  
  
# Install init.sh as init script  
COPY init.sh /etc/cont-init.d/  
  
# Download and extract s6 init  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.19.1.1/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
  

