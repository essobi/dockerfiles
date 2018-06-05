FROM phusion/baseimage:0.9.18  
MAINTAINER Vedran Vekić <inti.pacha@no.gmail.spam>  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
RUN apt-get update && \  
#Flac, Lame, FFMPEG, Oracle Java JDK  
apt-get install -y software-properties-common python-software-properties flac
lame && \  
add-apt-repository -y ppa:mc3man/trusty-media && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer ffmpeg maven git lintian fakeroot &&
\  
#Download Sources from Git  
git clone git://github.com/EugeneKay/subsonic.git && \  
cd /subsonic && \  
git checkout release && \  
#Build Sources from Scratch  
mvn package && \  
mvn -P full -pl subsonic-booter -am install && \  
mvn -P full -pl subsonic-installer-debian/ -am install && \  
#Install Subsonic  
dpkg -i ./subsonic-installer-debian/target/subsonic-*.deb && \  
#Remove unnecessary files  
rm -r -f /subsonic /root/.m2 && \  
apt-get purge -y maven git lintian fakeroot software-properties-common python-
software-properties && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
RUN mv /var/subsonic /var/subsonic.default && \  
ln -s /data /var/subsonic  
  
# Don't fork to the background  
RUN sed -i "s/ > \${LOG} 2>&1 &//" /usr/share/subsonic/subsonic.sh  
  
VOLUME /data /media  
EXPOSE 4040  
EXPOSE 9412  
RUN mkdir /etc/service/subsonic  
ADD start.sh /etc/service/subsonic/run  
RUN chmod a+x /etc/service/subsonic/run  

