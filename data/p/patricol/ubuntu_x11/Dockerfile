FROM patricol/ubuntu_rdp:Cuda  
  
USER root  
  
# This should add things I want every GUI workspace to have, but that aren't
needed for setting up or validating the various connection methods.  
ENV PATH=/home/user/.local/share/umake/bin:$PATH  
  
RUN add-apt-repository -y ppa:lyzardking/ubuntu-make && \  
# For daily builds of umake  
add-apt-repository -y ppa:remmina-ppa-team/remmina-next && \  
apt-get update; \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
libgconf-2-4 \  
#Needed by atom but currently not installed by umake.  
libsecret-1-0 gnome-keyring \  
#Needed by IntelliJ IDEs to store credentials  
remmina \  
# For connecting to other VMs  
ubuntu-make && \  
# Adding umake because it's used by just about every sub-container; to install
IDEs.  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
su user -c "umake ide atom /home/user/.local/share/umake/ide/atom"  
#COPY --chown=user:user extras/*.dockitem
/home/user/.config/plank/dock1/launchers/#Not yet supported by docker hub's
automated builds, which use an outdated version of docker.  
COPY extras/*.dockitem /home/user/.config/plank/dock1/launchers/  
RUN chown -R user:user /home/user/.config/ && \  
echo "chmod +x /home/user/.local/share/applications/*.desktop" >>
/home/user/earlycommands.sh  
COPY extras/config.cson /home/user/.atom/  
RUN chown -R user:user /home/user/.atom/ && \  
chmod 0664 /home/user/.atom/config.cson && \  
su user -c "/home/user/.local/share/umake/bin/apm install file-icons
highlight-selected jumpy language-docker script sort-lines" && \  
su user -c "/home/user/.local/share/umake/bin/apm disable spell-check"  
  
ENV HOST_DIRECTORY /home/user/persistent  
RUN mkdir -p $HOST_DIRECTORY  
VOLUME ["/home/user/persistent"]  
  
USER user

