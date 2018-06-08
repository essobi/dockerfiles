FROM patricol/ubuntu_x11:18.04  
USER root  
  
RUN apt-get update; \  
apt-get install -y \  
g++ gcc make gdb gdbserver \  
cmake valgrind && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN su user -c "umake ide clion /home/user/.local/share/umake/ide/clion"  
#COPY --chown=user:user extras/*.dockitem
/home/user/.config/plank/dock1/launchers/#Not yet supported by docker hub's
automated builds, which use an outdated version of docker.  
COPY extras/*.dockitem /home/user/.config/plank/dock1/launchers/  
RUN chown -R user:user /home/user/.config/  
  
USER user

