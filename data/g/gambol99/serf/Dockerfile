#  
# Author: Rohith (gambol99@gmail.com)  
# Date: 2015-02-09 15:27:17 +0000 (Mon, 09 Feb 2015)  
#  
# vim:ts=2:sw=2:et  
#  
FROM progrium/busybox  
MAINTAINER Rohith <gambol99@gmail.com>  
  
RUN opkg-install unzip curl bash  
RUN curl -skL https://dl.bintray.com/mitchellh/serf/0.6.3_linux_amd64.zip >
0.6.3_linux_amd64.zip && \  
unzip 0.6.3_linux_amd64.zip && \  
chmod +x serf  
  
EXPOSE 7946  
ENTRYPOINT [ "./serf" ]  

