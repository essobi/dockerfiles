FROM ubuntu:14.04  
MAINTAINER Viktor Petersson <info@viktorpetersson.com>  
  
# Update apt-cache and install wget  
RUN apt-get update && apt-get install -y wget && apt-get clean  
  
# Fetch btsync  
RUN wget -O /tmp/btsync.tar.gz https://download-
cdn.getsyncapp.com/stable/linux-x64/BitTorrent-Sync_x64.tar.gz && \  
tar xvfz /tmp/btsync.tar.gz -C /usr/bin/ && rm /tmp/btsync.tar.gz && \  
rm -f /usr/bin/LICENSE.TXT  
  
# Print out the version (there is no version arg, so we grep for it)  
RUN /usr/bin/btsync --foobar | grep "BitTorrent Sync"  
  
# Add config file  
ADD includes/btsync.conf /sync/btsync.conf  
ADD includes/ui.conf /sync/ui.conf  
ADD includes/start.sh /start.sh  
  
# Run the boot script  
CMD /start.sh  
  
EXPOSE 55555/tcp  
EXPOSE 8888/tcp  

