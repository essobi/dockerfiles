FROM ubuntu:14.04  
MAINTAINER Aminov Lev <aminov.lev@itmh.ru>  
  
ENV CI true  
  
RUN apt-get update && apt-get install -y \  
apt-utils \  
git \  
ca-certificates \  
curl \  
openssh-client \  
php5-cli \  
php5-curl \  
php5-mcrypt \  
php5-imagick \  
php5-xdebug \  
\--no-install-recommends \  
&& rm -r /var/lib/apt/lists/*  
  
# Fix php5-mcrypt installation  
RUN cp /etc/php5/mods-available/mcrypt.ini \  
/etc/php5/cli/conf.d/  
  
# Add work user  
RUN adduser --quiet deployer  
RUN echo "deployer:deployer" | chpasswd  
  
# Copy bin files  
COPY /bin/docker-entrypoint.sh /  
COPY /bin/bootstrap.sh /bin/  
  
# Copy ssh config  
COPY /system/ssh_config /etc/ssh/  
  
# Prepare workspace  
RUN mkdir /deployer  
  
# Copy user data  
COPY /system/id_rsa /deployer/  
COPY /data/* /deployer/  
  
# Set-up access rights  
RUN chown -R deployer:deployer /deployer  
RUN chown deployer:deployer /docker-entrypoint.sh  
RUN chmod 0755 /deployer  
RUN chmod 0600 /deployer/id_rsa  
  
# Set-up defaults  
USER deployer  
VOLUME /deployer  
WORKDIR /home/deployer  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

