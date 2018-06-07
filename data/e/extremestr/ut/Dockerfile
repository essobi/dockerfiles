FROM ubuntu:latest  
MAINTAINER ExtremeSTR  
ENTRYPOINT ["/bin/bash"]  
# Install components  
ADD
http://download.ap.bittorrent.com/track/beta/endpoint/utserver/os/linux-x64-ubuntu-13-04
/tmp/utserver.tar.gz  
RUN tar -zxvf /tmp/utserver.tar.gz -C /opt/  
RUN chown root:root -R /opt/utorrent-server-alpha-v3_3/  
RUN ln -s /opt/utorrent-server-alpha-v3_3/utserver /usr/bin/utserver  
  
# Expose ports  
EXPOSE 8080  
CMD ["/opt/utorrent-server-alpha-v3_3/utserver", "/usr/bin/utserver"]  

