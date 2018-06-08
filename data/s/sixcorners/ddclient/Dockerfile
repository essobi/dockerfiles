FROM debian  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
ddclient \  
ca-certificates \  
libjson-any-perl \  
&& rm -rf /var/lib/apt/lists/* \  
&& chown daemon:daemon /var/cache/ddclient \  
&& chown :daemon /etc/ddclient.conf \  
&& chmod g+r /etc/ddclient.conf  
COPY docker-entrypoint.sh /usr/local/bin/  
USER daemon  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["ddclient"]  

