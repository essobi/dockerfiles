FROM julienbayle/publik-docker-base  
  
MAINTAINER Julien BAYLE <julien.bayle@loire-atlantique.fr>  
  
# INSTALL COMBO  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
postgresql- \  
combo \  
publik-base-theme \  
&& rm -rf /var/lib/apt/lists/*  
  
# COMBO CONFIG  
COPY combo.settings.py /etc/combo/settings.d/loire-atlantique.py  
RUN cp /tmp/secret /etc/combo \  
&& chmod 755 /etc/combo/secret  
  
# NGINX CONFIG  
COPY nginx.template /etc/nginx/conf.d/combo.template  
  
# USEFULL TO BE ABLE TO RUN THE MANAGER  
RUN usermod combo -s /bin/bash  
  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 8080  
CMD ["/bin/bash"]  

