FROM shawn/ubuntu-saucy-i386  
MAINTAINER Shawn Tan  
  
ENV DISPLAY 172.17.42.1:0  
RUN sed -i 's/archive.ubuntu.com/us-west-1.ec2.archive.ubuntu.com/g'
/etc/apt/sources.list  
  
RUN touch /dev/fuse  
RUN apt-get update; apt-get install -y firefox openjdk-7-jre icedtea-7-plugin;
apt-get clean  
  
ENTRYPOINT ["/usr/bin/firefox"]  

