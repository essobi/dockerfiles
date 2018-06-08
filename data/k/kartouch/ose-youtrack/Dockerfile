FROM centos:latest  
MAINTAINER Christophe Augello <christophe@augello.be>  
  
#Variables  
ENV YOUTRACK_VERSION=6.5.17105  
ENV YOUTRACK_HOME /opt/youtrack  
  
#Create path/user/group  
RUN mkdir -p "$YOUTRACK_HOME"/{bin,data,backup,certs} && \  
groupadd youtrack -g 55 && \  
useradd youtrack -u 55 -g 55 -G youtrack -s /sbin/nologin -d "$YOUTRACK_HOME"
&& \  
test "$(id youtrack)" = "uid=55(youtrack) gid=55(youtrack)
groups=55(youtrack)" && \  
yum -y install java-1.8.0-openjdk.x86_64 wget && \  
yum clean all && rm -rf /var/cache/yum/*  
  
RUN wget -nv
https://download.jetbrains.com/charisma/youtrack-$YOUTRACK_VERSION.jar -O
/opt/youtrack/bin/youtrack.jar  
  
# Loosen permission bits to avoid problems running container with arbitrary
UID  
RUN chown -R youtrack.0 $YOUTRACK_HOME && chmod -R g+rwx $YOUTRACK_HOME  
  
EXPOSE 8080  
WORKDIR $YOUTRACK_HOME  
VOLUME ["/opt/youtrack/data", "/opt/youtrack/backup"]  
USER 55  
CMD ["java", \  
"-Xmx1g", \  
"-XX:MaxPermSize=512m", \  
"-Djava.awt.headless=true", \  
"-Duser.home=/opt/youtrack", \  
"-Djetbrains.youtrack.disableBrowser=true", \  
"-Djetbrains.youtrack.enableGuest=false", \  
"-Ddatabase.location=/opt/youtrack/data", \  
"-Ddatabase.backup.location=/opt/youtrack/backup", \  
"-jar", \  
"/opt/youtrack/bin/youtrack.jar", \  
"8080"]  

