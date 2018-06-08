FROM haugene/transmission-openvpn:latest  
  
ENV FILEBOT_VERSION 4.7.9  
ENV JAVA_OPTS "-Dsun.jnu.encoding=UTF-8 -Dfile.encoding=UTF-8 -DuseGVFS=false
-Djava.net.useSystemProxies=false -Dapplication.deployment=docker
-Dapplication.dir=/data -Duser.home=/data -Djava.io.tmpdir=/data/tmp
-Djava.util.prefs.PreferencesFactory=net.filebot.util.prefs.FilePreferencesFactory
-Dnet.filebot.util.prefs.file=/data/prefs.properties"  
RUN add-apt-repository ppa:openjdk-r/ppa -y \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends openjdk-8-jre mediainfo
libchromaprint-tools \  
&& ln -s java-8-openjdk-amd64 /usr/lib/jvm/default-jvm  
  
# Install filebot  
RUN
FILEBOT_SHA256=892723dcec8fe5385ec6665db9960e7c1a88e459a60525c02afb7f1195a50523
\  
&& FILEBOT_PACKAGE=filebot_${FILEBOT_VERSION}_amd64.deb \  
&& curl -L -O
https://downloads.sourceforge.net/project/filebot/filebot/FileBot_$FILEBOT_VERSION/$FILEBOT_PACKAGE
\  
&& echo "$FILEBOT_SHA256 *$FILEBOT_PACKAGE" | sha256sum --check --strict \  
&& dpkg -i $FILEBOT_PACKAGE \  
&& rm $FILEBOT_PACKAGE  
  
VOLUME /output  
  
# Run openvpn script  
CMD ["dumb-init", "/etc/openvpn/start.sh"]  

