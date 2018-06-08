FROM patricol/sfml:18.04  
USER root  
  
#COPY --chown=user:user extras/*.sh /home/user/#Not yet supported by docker
hub's automated builds, which use an outdated version of docker.  
COPY extras/*.sh /home/user/  
RUN chmod +x /home/user/*.sh && \  
chown -R user:user /home/user/*.sh  
  
#COPY --chown=user:user extras/*.dockitem
/home/user/.config/plank/dock1/launchers/#Not yet supported by docker hub's
automated builds, which use an outdated version of docker.  
COPY extras/*.dockitem /home/user/.config/plank/dock1/launchers/  
#COPY --chown=user:user extras/*.desktop
/home/user/.local/share/applications/#Not yet supported by docker hub's
automated builds, which use an outdated version of docker.  
COPY extras/*.desktop /home/user/.local/share/applications/  
RUN chown -R user:user /home/user/.config/ /home/user/.local/  
  
USER user

