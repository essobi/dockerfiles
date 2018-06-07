FROM julienbayle/publik-docker-base  
  
MAINTAINER Julien BAYLE <julien.bayle@loire-atlantique.fr>  
  
# INSTALL HOBO (without postgresql)  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
zip \  
postgresql- \  
hobo \  
publik-base-theme \  
&& rm -rf /var/lib/apt/lists/*  
  
# COPY conf files  
COPY site-options.cfg *.template /tmp/  
COPY hobo.settings.py /etc/hobo/settings.d/loire-atlantique.py  
  
# This user is required to use hobo-manage  
RUN usermod hobo -s /bin/bash  
  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 8080  
CMD ["/bin/bash"]  

