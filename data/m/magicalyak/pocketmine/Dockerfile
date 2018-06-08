# Minecraft PE Server  
FROM phusion/baseimage:0.9.19  
MAINTAINER Tom Gamull <tom.gamull@gmail.com>  
  
# Secure and init  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
CMD ["/sbin/my_init"]  
  
# Update, Install Prerequisites  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y update && \  
apt-get install -y \  
wget \  
libtool \  
autoconf \  
perl \  
autoconf \  
gcc-multilib && \  
apt-get install -y \  
language-pack-en-base \  
software-properties-common \  
python-software-properties && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Stage Files  
COPY server.properties /server.properties.original  
COPY entrypoint.sh /entrypoint.sh  
ENV PHP_BINARY /data/bin/php7/bin/php  
  
# Setup User  
RUN useradd -d /data -s /bin/bash --uid 1000 minecraft  
RUN chmod +x /entrypoint.sh  
RUN chown minecraft:minecraft /entrypoint.sh  
  
# Setup container  
EXPOSE 19132  
# Start Pocketmine  
#CMD ["/data/start.sh", "--no-wizard"]  
ENTRYPOINT ["/entrypoint.sh"]  

