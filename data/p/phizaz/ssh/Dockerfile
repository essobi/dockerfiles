FROM debian:jessie  
MAINTAINER Konpat Preechakul <the.akita.ta@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends openssh-client  
  
VOLUME ["/ssh"]  
  
# keep alive  
RUN echo "ServerAliveInterval 60" >> /etc/ssh/ssh_config  
  
COPY entrypoint.sh /usr/local/bin/  
RUN ln -s /usr/local/bin/entrypoint.sh /  
ENTRYPOINT ["entrypoint.sh"]  

