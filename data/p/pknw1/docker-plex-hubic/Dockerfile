FROM pknw1/hubicfuse:latest  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Install required packages  
ENV HOME /root  
ADD files/allowedNetworks.sh /etc/my_init.d/98allowedNetworks.sh  
ADD files/run.sh /etc/my_init.d/99application.sh  
  
RUN useradd --system --uid 797 -M --shell /usr/sbin/nologin plex  
  
# Hack to avoid install to fail due to upstart not being installed.  
# We won't use upstart anyway.  
RUN touch /bin/start  
RUN chmod +x /bin/start  
  
# Download and install Plex (non plexpass)  
# This gets the latest non-plexpass version  
RUN DOWNLOAD_URL=`curl -Ls https://plex.tv/downloads | grep -o
'[^"'"'"']*amd64.deb' | grep -v binaries` && \  
echo $DOWNLOAD_URL && \  
curl -L $DOWNLOAD_URL -o plexmediaserver.deb  
RUN dpkg -i plexmediaserver.deb  
RUN rm -f plexmediaserver.deb  
  
# Hack clean-up  
RUN rm -f /bin/start  
  
# Create writable config directory in case the volume isn't mounted  
USER root  
RUN usermod plex -G root  
  
#USER plex  
EXPOSE 32400  

