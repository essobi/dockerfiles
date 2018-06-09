FROM debian:jessie  
MAINTAINER Keith Bentrup <kbentrup@ebay.com>  
  
ENV LANG=en_US.UTF-8 \  
TERM=xterm-256color  
  
EXPOSE 22 443  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y stunnel4 && \  
openssl genrsa > /root/stunnel.key && \  
openssl req -new -key /root/stunnel.key -x509 -days 9999 -out
/root/stunnel.crt -subj "/C=US" && \  
cat /root/stunnel.* > /etc/stunnel/stunnel.pem && \  
chmod 600 /etc/stunnel/stunnel.pem  
  
COPY stunnel /etc/default/  
COPY *.sh /  

