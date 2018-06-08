FROM linuxserver/baseimage.python  
  
ENV APTLIST="nodejs"  
# install packages  
RUN curl -sL https://deb.nodesource.com/setup_0.12 | bash - && \  
apt-get install $APTLIST -qy && \  
  
# clean up  
apt-get clean && rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*  
  
# Adding Custom files  
ADD defaults/ /defaults/  
ADD init/ /etc/my_init.d/  
ADD services/ /etc/service/  
RUN chmod -v +x /etc/service/*/run && chmod -v +x /etc/my_init.d/*.sh  
  
# ports and volumes  
VOLUME /config  
EXPOSE 88 443  

