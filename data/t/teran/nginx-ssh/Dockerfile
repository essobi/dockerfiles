FROM nginx  
MAINTAINER Igor Shishkin <me@teran.ru>  
  
EXPOSE 22 80  
RUN apt-get update && \  
apt-get install -y --no-install-suggests --no-install-recommends \  
openssh-server \  
supervisor && \  
apt-get clean && \  
rm -rvf /var/lib/apt/lists/* && \  
rm -vf /etc/ssh/ssh_host_*  
  
RUN useradd -s /bin/sh publisher -d /home/publisher -m && \  
mkdir -p /public /run/sshd /home/publisher/.ssh && \  
chown publisher:publisher /public /home/publisher/.ssh  
  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

