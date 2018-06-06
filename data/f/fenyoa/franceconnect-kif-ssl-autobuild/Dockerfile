From fenyoa/franceconnect-kif  
MAINTAINER Alexandre Fenyo <alex@fenyo.net>  
EXPOSE 443  
RUN apt-get update && apt-get install -y --allow-downgrades --allow-remove-
essential --allow-change-held-packages apache2 curl  
WORKDIR /etc/apache2  
RUN rm sites-enabled/000-default.conf && cp -p sites-available/default-
ssl.conf sites-enabled && cp -p mods-available/proxy.load mods-
available/proxy_ajp.load mods-available/ssl.conf mods-available/ssl.load mods-
available/socache_shmcb.load mods-enabled  
RUN echo ServerName localhost >> apache2.conf  
WORKDIR "/kif"  
CMD apachectl start && mvn -Dmaven.tomcat.ajp.port=8009
-Dnet.fenyo.franceconnect.config.listen.port=8080 tomcat7:run  

