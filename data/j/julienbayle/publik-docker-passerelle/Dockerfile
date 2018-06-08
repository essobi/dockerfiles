FROM julienbayle/publik-docker-base  
  
MAINTAINER Julien BAYLE <julien.bayle@loire-atlantique.fr>  
  
# INSTALL PUBLIK  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
postgresql- \  
passerelle \  
&& rm -rf /var/lib/apt/lists/*  
  
# CONFIGURE MODULES  
COPY passerelle.settings.py /etc/passerelle/settings.d/loire-atlantique.py  
  
# NGINX CONF FOR PUBLIC  
COPY nginx.template /etc/nginx/conf.d/passerelle.conf  
  
# USEFULL TO BE ABLE TO USE THE MANAGER  
RUN usermod passerelle -s /bin/bash  
  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 8080  
CMD ["/bin/bash"]  

