FROM hurricane/dockergui:x11rdp  
#FROM hurricane/dockergui:x11rdp  
#FROM hurricane/dockergui:xvnc  
  
MAINTAINER David Coppit <david@coppit.org>  
  
ENV APP_NAME="Filebot" WIDTH=1280 HEIGHT=720 TERM=xterm  
  
# User/Group Id gui app will be executed as  
ENV USER_ID=99  
ENV GROUP_ID=100  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN \  
# Speed up APT  
echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup && \  
echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache && \  
# Auto-accept Oracle JDK license  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
# Filebot needs Java 8  
add-apt-repository ppa:webupd8team/java && \  
apt-get update && \  
# Install a specific version for reproducible builds  
apt-get install -qy 'oracle-java8-installer=8u131-1~webupd8~2' && \  
# clean up  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
/usr/share/man /usr/share/groff /usr/share/info \  
/usr/share/lintian /usr/share/linda /var/cache/man && \  
(( find /usr/share/doc -depth -type f ! -name copyright|xargs rm || true )) &&
\  
(( find /usr/share/doc -empty|xargs rmdir || true ))  
  
VOLUME ["/input", "/output", "/config"]  
  
EXPOSE 3389 8080  
## I'm not sure if these are actually needed, but they suppress some Java
exceptions  
#RUN apt-get update \  
# && apt-get install -y libxslt1-dev libgl1-mesa-dev \  
# && apt-get clean  
#  
## Suppress some errors in the log  
#RUN mkdir -p /var/lib/tomcat7/logs  
# Set the locale, to support files that have non-ASCII characters  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
COPY startapp.sh /startapp.sh  
  
RUN \  
# Create dir to keep things tidy. Make sure it's readable by $USER_ID  
mkdir /files && \  
chmod a+rwX /files && \  
# To find the latest version:
https://www.filebot.net/download.php?mode=s&type=deb&arch=amd64  
# We'll use a specific version for reproducible builds  
wget -N
'https://sourceforge.net/projects/filebot/files/filebot/FileBot_4.7.9/filebot_4.7.9_amd64.deb'
-O /files/filebot.deb && \  
dpkg -i /files/filebot.deb && rm /files/filebot.deb && \  
  
mkdir -p /nobody/.java/.userPrefs/net/filebot && \  
ln -s /nobody/.java/.userPrefs/net/filebot /config && \  
# Otherwise RDP rendering of the UI doesn't work right.  
sed -i 's/java /java -Dsun.java2d.xrender=false /' /usr/bin/filebot  

