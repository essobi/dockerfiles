FROM debian:jessie  
ENV DEBIAN_FRONTEND noninteractive  
  
MAINTAINER muze-nl  
  
RUN sed -e 's@main$@main contrib non-free@' -i /etc/apt/sources.list  
  
# Commands  
RUN \  
apt-get update && \  
apt-get --no-install-recommends install -y openssh-client php5-cli curl ca-
certificates git sed rsync && \  
apt-get --no-install-recommends install -y npm nodejs-legacy nodejs bzip2 && \  
apt-get upgrade -y && \  
apt-get clean && \  
rm -r /var/lib/apt/lists/*  
  
RUN \  
curl --max-redirs 3 -o /tmp/composer-install
https://raw.githubusercontent.com/composer/getcomposer.org/master/web/installer
&& php /tmp/composer-install --install-dir=/usr/local/bin/ --filename=composer
&& rm /tmp/composer-install  
  
RUN \  
curl --max-redirs 3 https://deployer.org/releases/v3.3.0/deployer.phar -o
/usr/local/bin/dep && \  
chmod a+rx /usr/local/bin/dep && \  
/bin/echo -e "Host *\n\tStrictHostKeyChecking no\n\tPasswordAuthentication
no\n\n" | tee -a /etc/ssh/ssh_config  
  

