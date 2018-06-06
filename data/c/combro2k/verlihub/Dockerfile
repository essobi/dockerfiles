FROM ubuntu-debootstrap:14.04  
MAINTAINER Martijn van Maurik <docker@vmaurik.nl>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
  
RUN apt-get update && apt-get dist-upgrade -yq && \  
apt-get install python-dev liblua5.1-0-dev git \  
libpcre3-dev libssl-dev mysql-client libmysqlclient-dev \  
g++ libgeoip-dev gettext cmake wget -yq && \  
apt-get clean -y && \  
apt-get autoclean -y && \  
rm -fr /var/lib/apt && \  
git clone https://github.com/Verlihub/verlihub-1.0.0.git /usr/src/verlihub &&
\  
cd /usr/src/verlihub && chmod +x ./configure && ./configure --prefix=/usr && \  
make && make install  
  
ADD start.sh /usr/local/bin/start.sh  
  
RUN chmod +x /usr/local/bin/start.sh  
  
EXPOSE 4111  
ENTRYPOINT ["/usr/local/bin/start.sh"]  
  
CMD ["--run"]  

