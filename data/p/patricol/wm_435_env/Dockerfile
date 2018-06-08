FROM patricol/android:16.04  
USER root  
RUN su user -c "umake ide eclipse /home/user/.local/share/umake/ide/eclipse"  
  
#COPY --chown=user:user extras/MainGUI.sh /home/user/#Not yet supported by
docker hub's automated builds, which use an outdated version of docker.  
COPY extras/MainGUI.sh /home/user/  
RUN chmod +x /home/user/MainGUI.sh && \  
chown -R user:user /home/user/MainGUI.sh  
  
#COPY --chown=user:user extras/*.dockitem
/home/user/.config/plank/dock1/launchers/#Not yet supported by docker hub's
automated builds, which use an outdated version of docker.  
COPY extras/*.dockitem /home/user/.config/plank/dock1/launchers/  
#COPY --chown=user:user extras/*.desktop
/home/user/.local/share/applications/#Not yet supported by docker hub's
automated builds, which use an outdated version of docker.  
COPY extras/*.desktop /home/user/.local/share/applications/  
RUN chown -R user:user /home/user/.config/ /home/user/.local/  
  
ENV GPUTOGGLE=on  
  
USER user

