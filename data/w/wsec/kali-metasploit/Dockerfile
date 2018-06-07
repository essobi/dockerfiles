# Docker container with metasploit.  
# Based on linuxkonsult/kali-metasploit and slightly modified  
# Use Kali Linux official Docker  
FROM kalilinux/kali-linux-docker  
MAINTAINER Filip Waeytens "filip@wsec.be"  
ENV DEBIAN_FRONTEND noninteractive  
  
#/init.sh just runs msfupdate and msfconsole  
ADD ./init.sh /init.sh  
RUN chmod +x /init.sh  
# Install metasploit  
RUN apt-get -y update ; apt-get -y --force-yes install libnokogiri-ruby
metasploit-framework  
  
# Attach this container to stdin when running, like this:  
# docker run --net=host -t -i linux/kali/metasploit  
#--net=host allows listening to incoming connections on the host ip  
CMD /init.sh  

