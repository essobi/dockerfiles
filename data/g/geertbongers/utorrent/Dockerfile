# Docker utorrent server  
FROM geertbongers/home-user  
MAINTAINER Geert  
  
ADD http://download-
new.utorrent.com/endpoint/utserver/os/linux-x64-ubuntu-13-04/track/beta/
/tmp/utserver.tar.gz  
RUN mkdir -p /utorrent_install && tar -zvxf /tmp/utserver.tar.gz -C
/utorrent_install/ &&\  
chown -R home_user:home_user /utorrent_install/$(ls /utorrent_install/|tail
-1) &&\  
cd /utorrent_install/ && ln -s /utorrent_install/$(ls /utorrent_install/|tail
-1) /utorrent &&\  
rm -f /tmp/utorrent.tar.gz &&\  
chown -R home_user:home_user /utorrent &&\  
mkdir /container-data &&\  
chown -R home_user:home_user /container-data  
  
# Expose the port (you also need to portmap this if you're behind a NAT
router)  
EXPOSE 6881  
EXPOSE 6881/udp  
# Expose the web interface  
EXPOSE 9088  
VOLUME /container-data  
  
USER home_user  
CMD /bin/bash  
#CMD ["-configfile", "/container-data/settings.conf", "-settingspath",
"/container-data/default.log"]  
#ENTRYPOINT ["dockerize", "-stdout", "/container-data/default.log",
"/utorrent/utserver"]  

