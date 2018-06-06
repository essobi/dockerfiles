FROM tozd/postfix  
  
VOLUME /etc/sympa/shared  
  
RUN apt-get update -q -q && \  
apt-get install adduser openssh-client \--yes \--force-yes && \  
adduser \--system \--group mailpipe \--no-create-home \--home /nonexistent &&
\  
cp /etc/postfix/main.cf /etc/postfix/main.cf.orig && \  
cp /etc/postfix/master.cf /etc/postfix/master.cf.orig  
  
COPY ./etc /etc  

