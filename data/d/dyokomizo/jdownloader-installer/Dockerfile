FROM ubuntu:xenial  
MAINTAINER Daniel Yokomizo <daniel.yokomizo@gmail.com>  
  
RUN apt-get update \  
&& apt-get install --yes \  
nano \  
openjdk-9-jre \  
wget  
  
COPY JD2SilentSetup_x64.sh.sha512 /opt/JD2SilentSetup_x64.sh.sha512  
  
RUN wget --quiet --directory-prefix=/opt
http://installer.jdownloader.org/JD2SilentSetup_x64.sh \  
&& sha512sum --check /opt/JD2SilentSetup_x64.sh.sha512 \  
&& rm /opt/JD2SilentSetup_x64.sh.sha512 \  
&& chmod +x /opt/JD2SilentSetup_x64.sh  
  
CMD ["/opt/JD2SilentSetup_x64.sh"]  

