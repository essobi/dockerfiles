FROM debian:jessie-slim  
MAINTAINER thunderball  
  
EXPOSE 25  
RUN echo "postfix postfix/main_mailer_type string Internet Site" | debconf-
set-selections && \  
apt-get update && apt-get --no-install-recommends install -y postfix  
  
VOLUME /var/spool/postfix  
  
COPY entrypoint /entrypoint  
  
ENTRYPOINT ["/entrypoint"]  

