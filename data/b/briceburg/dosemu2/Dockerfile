FROM briceburg/dosemu2:debian  
  
#  
# dex dosemu2 image  
#  
# see dosemu2 manpage for flags,  
# https://github.com/stsp/dosemu2/tree/devel/man  
ENV \  
DOSEMU_CMD="dir" \  
DOSEMU_FLAGS="-E"  
COPY dex/autoexec.bat /etc/dosemu/drives/c/autoexec.bat  
COPY dex/entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
# allow writable c:\  
RUN chmod -R 777 /etc/dosemu/drives/c  
  
#  
# v1 dex-api  
#  
# dex ( https://github.com/dockerland/dex )  
# * prefer common home in derivatives.  
# * default to interactive tty, sharing tty0 to allow console layout
detection.  
# * mount host root to /dex/workspace (autoexec.bat mounts as R:)  
LABEL \  
org.dockerland.dex.api="v1" \  
org.dockerland.dex.docker_devices="tty0" \  
org.dockerland.dex.docker_flags="-it" \  
org.dockerland.dex.docker_groups="tty" \  
org.dockerland.dex.docker_home="dosemu2" \  
org.dockerland.dex.docker_workspace="/"  

