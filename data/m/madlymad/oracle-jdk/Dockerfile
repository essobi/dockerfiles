# Pull base image.  
FROM debian:wheezy  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set the locale  
RUN \  
apt-get update && apt-get install -y --no-install-recommends locales &&\  
rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/* /var/cache/debconf/*-old
&&\  
localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8  
ENV LANG en_US.utf8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
# Install Deps  
# - http://www.oracle.com/technetwork/java/javase/jre-8-readme-2095710.html  
RUN \  
echo deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main | tee
/etc/apt/sources.list.d/webupd8team-java.list &&\  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&\  
apt-get update &&\  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections &&\  
apt-get -y --no-install-recommends install oracle-java8-installer unzip procps
&&\  
rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/* /var/cache/debconf/*-old
/var/cache/oracle-jdk*-installer \  
${JAVA_HOME}/src.zip \  
${JAVA_HOME}/*-src.zip \  
${JAVA_HOME}/db \  
${JAVA_HOME}/lib/missioncontrol \  
${JAVA_HOME}/lib/visualvm \  
${JAVA_HOME}/lib/*javafx* \  
${JAVA_HOME}/jre/lib/plugin.jar \  
${JAVA_HOME}/jre/lib/ext/jfxrt.jar \  
${JAVA_HOME}/jre/bin/javaws \  
${JAVA_HOME}/jre/lib/javaws.jar \  
${JAVA_HOME}/jre/lib/desktop \  
${JAVA_HOME}/jre/plugin \  
${JAVA_HOME}/jre/lib/deploy* \  
${JAVA_HOME}/jre/lib/*javafx* \  
${JAVA_HOME}/jre/lib/*jfx* \  
${JAVA_HOME}/jre/lib/amd64/libdecora_sse.so \  
${JAVA_HOME}/jre/lib/amd64/libprism_*.so \  
${JAVA_HOME}/jre/lib/amd64/libfxplugins.so \  
${JAVA_HOME}/jre/lib/amd64/libglass.so \  
${JAVA_HOME}/jre/lib/amd64/libgstreamer-lite.so \  
${JAVA_HOME}/jre/lib/amd64/libjavafx*.so \  
${JAVA_HOME}/jre/lib/amd64/libjfx*.so  

