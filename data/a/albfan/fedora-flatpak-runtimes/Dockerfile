FROM fedora:25  
MAINTAINER Alberto Fanjul <albertofanjul@gmail.com>  
  
# Install flatpak packages  
RUN dnf -y update  
RUN dnf -y install flatpak flatpak-builder git  
  
# Install gnome runtimes  
ENV FLATPAK_OSTREE_REPO_MODE=user-only  
RUN flatpak remote-add --from gnome-nightly https://sdk.gnome.org/gnome-
nightly.flatpakrepo && flatpak install gnome-nightly org.gnome.Sdk && flatpak
install gnome-nightly org.gnome.Platform  
  
CMD ["bash"]  

