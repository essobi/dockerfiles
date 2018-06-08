FROM centos:7  
MAINTAINER Chris Straffon <muppet_3000@hotmail.com>  
  
RUN yum update -y && \  
yum install -y java-1.7.0-openjdk-headless initscripts && \  
yum install -y --nogpgcheck https://s3-eu-west-1.amazonaws.com/subsonic-
public/download/subsonic-6.1.3.rpm && \  
yum clean all && \  
rm -rf /var/tmp/*  
  
RUN groupadd -g 3002 music_admins && \  
groupadd -g 1004 subsonic_daemon && \  
useradd -r -g subsonic_daemon -G music_admins -u 1004 subsonic_daemon  
  
ADD subsonic /etc/sysconfig/subsonic  
RUN chown subsonic_daemon:subsonic_daemon /etc/sysconfig/subsonic  
  
# run in the foreground  
RUN sed -i "s/ > \${LOG} 2>&1 &//" /usr/share/subsonic/subsonic.sh  
  
VOLUME ["/var/subsonic","/media/music"]  
  
EXPOSE 4443  
CMD /etc/init.d/subsonic start && tail -f /var/subsonic/subsonic.log  

