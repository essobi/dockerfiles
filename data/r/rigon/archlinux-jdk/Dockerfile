# Arch Linux baseline docker container with Oracle JDK  
# Generated on Sep Aug 09 17:09:51 GMT 2016 using code in this GitHub repo:  
# https://github.com/rigon/docker-archlinux-jdk  
FROM base/archlinux:latest  
MAINTAINER Ricardo Gonçalves <ricardompgoncalves@gmail.com>  
  
# run script for JDK installation  
ADD setup-jdk.sh /usr/sbin/setup-jdk  
RUN setup-jdk  
  
# Add JDK bin dir to PATH  
ENV PATH=$PATH:/usr/lib/jvm/default/bin  

