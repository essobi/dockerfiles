FROM ubuntu:latest  
  
COPY svn.conf /etc/apache2/conf-enabled/  
COPY start.sh /srv  
  
RUN apt-get update && apt-get install -y \  
apache2 \  
apache2-utils \  
libapache2-mod-svn \  
subversion \  
&& rm -rf /var/lib/apt/lists/* \  
&& chmod 755 /srv/start.sh  
  
VOLUME [ "/mnt/subversion" ]  
  
EXPOSE 80  
ENTRYPOINT ["/bin/bash"]  
CMD ["/srv/start.sh"]  

