FROM centos:7  
MAINTAINER Chris Straffon <muppet_3000@hotmail.com>  
  
ADD schotty-plex.repo /etc/yum.repos.d/  
  
RUN groupadd -g 497 plex && useradd -c "RPM Created PlexUser" -d
"/var/lib/plexmediaserver" -s "/sbin/nologin" -r -g plex -u 497 plex  
  
RUN yum update -y && yum install -y initscripts plexmediaserver && yum clean
all  
  
ADD PlexMediaServer /etc/sysconfig/  
  
VOLUME
["/var/lib/plexmediaserver","/media/music","/media/tv","/media/films","/media/pictures"]  
  
EXPOSE 32400  
CMD rm /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\
Server/plexmediaserver.pid && /etc/init.d/plexmediaserver start && tail -f
/var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\
Server/Logs/Plex\ Media\ Server.log  

