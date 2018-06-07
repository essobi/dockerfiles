# Docker registry repo/image used as our base  
FROM ctarwater/kali  
  
# Who is responsible for this madness?  
MAINTAINER ctarwater@blackfinsecurity.com  
  
# Remove default sources.list  
RUN rm /etc/apt/sources.list  
  
# Update our sources.list  
ADD ./sources.list /etc/apt/sources.list  
  
# Add our script to start the metasploit console  
ADD ./init.sh /init.sh  
  
# Install stuff  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -y --force-yes install metasploit metasploit-framework sudo  
  
# Strip out unused Metasploit modules  
RUN rm -rf /usr/share/metasploit-framework/modules/*  
  
# Prepare the database  
RUN service postgresql start && \  
service metasploit start && \  
msfconsole  
  
# We need to run multiple commands to get the msf running, so we put them into
a single script  
CMD ["/init.sh"]

