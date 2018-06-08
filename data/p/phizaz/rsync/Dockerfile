FROM debian:jessie  
MAINTAINER Konpat Preechakul <the.akita.ta@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends rsync openssh-client  
  
VOLUME ["/ssh"]  
VOLUME ["/workdir"]  
  
WORKDIR /workdir  
  
COPY entrypoint.sh /usr/local/bin/  
RUN ln -s /usr/local/bin/entrypoint.sh /  
ENTRYPOINT ["entrypoint.sh"]  

