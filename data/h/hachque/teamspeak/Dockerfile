FROM hachque/systemd-none  
MAINTAINER June Rhodes  
  
# Install requirements  
RUN zypper --non-interactive in wget sudo  
  
# Add user  
RUN echo "teamspeak:x:1999:1999:user for teamspeak:/srv/teamspeak:/bin/bash"
>> /etc/passwd  
RUN echo "teamspeak:!:1999:" >> /etc/group  
  
# Expose TeamSpeak ports  
EXPOSE 30033  
EXPOSE 10011  
EXPOSE 9987  
EXPOSE 9988  
EXPOSE 9989  
# Add the start & install script  
# Because TeamSpeak is proprietary software, you'll need  
# to configure a URL to download TeamSpeak from for installation  
ADD 10-teamspeak /etc/init.simple/10-teamspeak  
  
# Set /init as the default  
CMD ["/init"]  

