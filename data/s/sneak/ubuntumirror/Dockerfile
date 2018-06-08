FROM phusion/baseimage:0.9.18  
  
VOLUME /var/mirror  
  
ADD ./sources.list /etc/apt/sources.list  
RUN echo "#!/bin/sh\nexit 101" > /usr/sbin/policy-rc.d  
# phusion baseimage says i'm not supposed to do this  
# and i don't care:  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y run-one nginx make debmirror  
  
ADD ./mirror /opt/mirror  
ADD ./mirror.run /etc/service/mirror/run  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD ./nginx.run /etc/service/nginx/run  
RUN chmod +x /etc/service/nginx/run && \  
chmod +x /etc/service/mirror/run  
RUN \  
export GNUPGHOME=/etc/debmirror/ubuntu && \  
mkdir -p $GNUPGHOME && \  
chmod go-rwx $GNUPGHOME && \  
gpg --import /usr/share/keyrings/ubuntu-archive-keyring.gpg && \  
cp $GNUPGHOME/pubring.gpg $GNUPGHOME/trustedkeys.gpg  
  
EXPOSE 80  

