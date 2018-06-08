FROM debian:sid  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y shellcheck  
USER nobody  
CMD shellcheck /scripts/script.sh  
  

