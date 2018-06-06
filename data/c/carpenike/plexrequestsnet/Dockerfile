# set base os  
FROM carpenike/mono  
  
MAINTAINER carpenike <carpenike@gmail.com>  
  
# set some environment variables for mariadb to give us our paths  
ENV INSTALL_LIST="unzip"  
# update apt and install packages  
RUN apt-get -qy update && \  
apt-get install \  
$INSTALL_LIST -qy && \  
plex_remote="$(curl -sX GET
https://api.github.com/repos/tidusjar/PlexRequests.Net/releases/latest | awk
'/tag_name/{print $4;exit}' FS='[""]')" && \  
rm -rf /app/PlexRequests.Net && \  
curl -o /tmp/plexrequestsnet.zip -L
https://github.com/tidusjar/PlexRequests.Net/releases/download/"$plex_remote"/PlexRequests.zip
&& \  
unzip -o /tmp/plexrequestsnet.zip -d /tmp && \  
mv /tmp/Release /app/PlexRequests.Net && \  
rm /tmp/plexrequestsnet.zip && \  
# clean up  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#Adding Custom files  
COPY services/ /etc/service/  
RUN chmod -v +x /etc/service/*/run /etc/my_init.d/*.sh  
  
# set volumes and ports  
VOLUME /config  
EXPOSE 3579  

