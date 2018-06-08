FROM debian:jessie  
MAINTAINER Milton Pividori <miltondp@gmail.com>  
  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-get update -y && apt-get install -y \--no-install-recommends \  
git \  
python3-uno \  
libreoffice-writer \  
libreoffice-calc \  
python3-pip \  
xvfb \  
supervisor \  
libreoffice-l10n-es \  
openjdk-7-jre \  
&& pip3 install jsonrpc2 daemonize \  
&& git clone https://github.com/aeroo/aeroo_docs.git /opt/aeroo_docs \  
&& apt-get purge -y \--auto-remove git \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 8989  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
CMD exec supervisord -c /etc/supervisor/conf.d/supervisord.conf  

