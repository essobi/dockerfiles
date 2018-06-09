# Tinyproxy for ARMv7 with transparent config  
# VERSION 1.0.0  
FROM mazzolino/armhf-ubuntu  
  
MAINTAINER pgeraghty  
  
RUN \  
apt-get update && \  
apt-get upgrade -y  
  
# Configure locales  
RUN locale-gen en_US.UTF-8  
  
# Set default locale for the environment  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
RUN \  
apt-get install -y tinyproxy && \  
  
apt-get autoremove -y && \  
apt-get clean all && \  
rm -rf /var/lib/apt/lists/*  
  
COPY tinyproxy.conf /etc/  
RUN mkdir -p /var/run/tinyproxy/ && chmod 777 /var/run/tinyproxy/  
  
USER nobody  
EXPOSE 8888  
# Default command  
ENTRYPOINT ["/usr/sbin/tinyproxy"]  
  
# do not daemonize  
CMD ["-d"]  

