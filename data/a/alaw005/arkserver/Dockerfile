FROM debian:jessie  
  
# Required for nano to work (to view files in container)  
ENV TERM=xterm  
  
# Install dependencies - refer http://ark.gamepedia.com/Dedicated_Server_Setup  
RUN apt-get update \  
&& apt-get install -y \  
curl \  
lib32gcc1 \  
nano \  
&& rm -rf /var/lib/apt/lists/*  
  
# Configure Open Files Limit - refer
http://ark.gamepedia.com/Dedicated_Server_Setup  
# NB: Does not apply "fs.file-max=100000" setting to "/etc/sysctl.conf" as  
# "sysctl -p /etc/sysctl.conf" cannot be executed in Docker image (read only
file system error)  
RUN echo "fs.file-max=100000" >> /etc/sysctl.conf \  
&& echo "* soft nofile 1000000" >> /etc/security/limits.conf \  
&& echo "* hard nofile 000000" >> /etc/security/limits.conf \  
&& echo "session required pam_limits.so" >> /etc/pam.d/common-session  
  
# Install steamcmd and assigned to steam user  
RUN mkdir -p /steam && cd steam \  
&& curl -sqL
'https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz' | tar
zxvf -  
  
EXPOSE 7777/udp  
EXPOSE 7778/udp  
EXPOSE 27015/udp  
  
# Create volume for ark server and assign to steam user  
VOLUME /arkserver  
  
COPY docker-entrypoint.sh /steam/  
RUN chmod +x /steam/docker-entrypoint.sh  
  
# TODO: Should be entrypoint script that run commands against  
CMD ["/steam/docker-entrypoint.sh"]  

