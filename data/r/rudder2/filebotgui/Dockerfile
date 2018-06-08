# FileBotGUI over VNC  
# Builds a docker gui image  
FROM hurricane/dockergui:xvnc  
  
# Set environment variables  
# User/Group Id gui app will be executed as default are 99 and 100  
ENV USER_ID=99  
ENV GROUP_ID=100  
# Gui App Name default is "GUI_APPLICATION"  
ENV APP_NAME="FileBotGUI"  
# Default resolution, change if you like  
ENV WIDTH=1280  
ENV HEIGHT=720  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Remove built-in Java 7  
RUN apt-get purge -y openjdk-\\* icedtea\\*  
  
# Auto-accept Oracle JDK license  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
  
# Install Java 8  
RUN add-apt-repository ppa:webupd8team/java \  
&& apt-get update \  
&& apt-get install -y oracle-java8-installer \  
&& apt-get clean  
  
#Install FileBotUI  
# To find the latest version:
https://www.filebot.net/download.php?mode=s&type=deb&arch=amd64  
# We'll use a specific version for reproducible builds  
RUN set -x \  
&& wget -N
'http://downloads.sourceforge.net/project/filebot/filebot/FileBot_4.6/filebot_4.6_amd64.deb'
-O /root/filebot.deb \  
&& dpkg -i /root/filebot.deb && rm /root/filebot.deb \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# set volumes  
VOLUME /Input /Output  
  
# Expose Port  
EXPOSE 8080  

