from alpine:3.5  
RUN apk add --no-cache bash openssh findutils php5-json php5-phar git && \  
apk add --no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/community/ emacs && \  
apk add --no-cache --repository http://nl.alpinelinux.org/alpine/edge/testing
global cscope && \  
rm -rf /var/cache/apk/*  
  
RUN echo "export TERM=xterm" >> /root/.bashrc  
  
COPY emacs.sh /usr/bin/e  
RUN chmod -R 777 /usr/bin/e  
RUN cd /root && mkdir .ssh && chmod -R 700 /root/.ssh  
RUN echo "PasswordAuthentication no" > /etc/ssh/sshd_config  
RUN touch /authorized_keys  
  
CMD /usr/sbin/sshd -D  

