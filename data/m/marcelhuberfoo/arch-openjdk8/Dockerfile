FROM marcelhuberfoo/arch  
MAINTAINER Marcel Huber <marcelhuberfoo@gmail.com>  
  
USER root  
  
RUN pacman -Syy -q --noconfirm jre8-openjdk-headless java-rhino jdk8-openjdk
p7zip gtk2 \  
gnome-themes-standard fontconfig ttf-droid ttf-dejavu ttf-freefont && \  
printf "y\\\ny\\\n" | pacman -Scc  
  
# Add support for extra strength cryptographic ciphers  
RUN curl -L --cookie "oraclelicense=accept-securebackup-cookie;"
http://download.oracle.com/otn-pub/java/jce/8/jce_policy-8.zip -O && \  
7z e -y -o/usr/lib/jvm/$(archlinux-java get)/jre/lib/security
/jce_policy-8.zip && \  
rm /jce_policy-8.zip  
  

