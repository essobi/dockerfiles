FROM fedora:26  
RUN dnf install -y mock yum yum-utils \  
&& echo "config_opts['use_nspawn'] = False" >> /etc/mock/site-defaults.cfg \  
&& dnf clean all  
  
RUN curl -LsS "https://github.com/tianon/gosu/releases/download/1.10/gosu-
amd64" > /usr/sbin/gosu \  
&& chmod +x /usr/sbin/gosu  
  
VOLUME /var/lib/mock  
VOLUME /var/cache/mock  
  
COPY entrypoint.sh /entrypoint  
  
ENTRYPOINT [ "/entrypoint" ]  
CMD [ "mock" ]  

