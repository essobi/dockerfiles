FROM owncloud  
  
# Bereite Download vor...  
RUN apt-get update && apt-get install -y wget  
  
# Download und Installation von dockerize  
ENV DOCKERIZE_VERSION v0.5.0  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
## Stelle das Skript move_uid_and_gid.sh im Container bereit  
COPY assets/move_uid_and_gid.sh /  
  
# Kopiere den neuen Entrypoint in den Container und aktiviere ihn...  
COPY assets/my_entrypoint.sh /  
ENTRYPOINT ["/my_entrypoint.sh"]  
CMD ["apache2-foreground"]  

