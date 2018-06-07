# escape=`  
FROM hydrologist/steamcmd:latest  
  
LABEL maintainer="Michael Dai <mik99935@.com>"  
  
HEALTHCHECK NONE  
  
# Copy entry point script  
COPY ./docker-entrypoint.sh /home/steam/docker-entrypoint.sh  
  
# Install dependencies  
RUN chown steam /home/steam/docker-entrypoint.sh &&`  
chmod +x /home/steam/docker-entrypoint.sh &&`  
apt-get update &&`  
apt-get upgrade -y &&`  
apt-get install -y`  
zlib1g:i386`  
openssl:i386`  
libssh2-1:i386`  
libgcc1:i386`  
libz1:i386`  
libcurl4-gnutls-dev:i386`  
tmux`  
libncurses5:i386`  
libbz2-1.0:i386`  
libasound2:i386  
  
USER steam  
  
# Install Team Fortress 2  
RUN /home/steam/steamcmd`  
+login anonymous`  
+force_install_dir /home/steam/tf2`  
+app_update 232250 validate`  
+quit  
  
# Symlink a library  
RUN mkdir /home/steam/.steam/sdk32 &&`  
ln -s /home/steam/tf2/bin/steamclient.so
/home/steam/.steam/sdk32/steamclient.so  
  
ENV TF2_PORT=27015  
  
# Expose the server ports  
EXPOSE ${TF2_PORT}/tcp ${TF2_PORT}/udp  
  
ENTRYPOINT ["/home/steam/docker-entrypoint.sh"]  
  
CMD ["-game tf", "+quit"]  
  
ONBUILD ENTRYPOINT ["/bin/bash"]  
  
ONBUILD USER ROOT  

