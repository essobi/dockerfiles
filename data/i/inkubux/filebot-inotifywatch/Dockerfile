FROM java:openjdk-8-jre  
  
MAINTAINER Francis Belanger "francis.belanger@gmail.com"  
RUN apt-get update && apt-get install -y inotify-tools  
  
# install mediainfo  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y mediainfo && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# download and install filebot  
RUN URL='https://www.filebot.net/download.php?mode=s&type=deb&arch=amd64';
FILE=`mktemp`; wget "$URL" -qO $FILE && dpkg -i $FILE; rm $FILE  
  
ADD startup.sh /  
ADD filebot.sh /  
ADD postprocess.sh /  
  
VOLUME /config  
VOLUME /media  
VOLUME /watch  
VOLUME /downloads  
  
ENTRYPOINT ["/startup.sh"]  

