FROM debian:jessie  
  
ENV TZ=Asia/Tokyo \  
VERSION=4_1_0  
  
RUN apt-get update \  
&& apt-get install -y wget expect \  
&& wget -O /usr/local/src/googleappsdirsync.sh
"https://dl.google.com/dirsync/google/googleappsdirsync_linux_64bit_${VERSION}.sh"  
  
ADD expect.sh /usr/local/src/expect.sh  
  
RUN /usr/local/src/expect.sh  
  
WORKDIR /usr/local/GoogleAppsDirSync

