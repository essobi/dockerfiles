# This Dockerfile makes a basic Gentoo Studio image without any audio/midi
software installed,  
# to be used as a basis for testing ebuilds added to the GentooStudio overlay.  
# Run docker pull gentoo/stage3-amd64 before running "docker build -t
gentoostudio ."  
FROM gentoo/stage3-amd64  
  
# Bring Portage up to date  
RUN mkdir -p /etc/portage/repos.conf  
COPY gentoo.conf /etc/portage/repos.conf/  
RUN emerge-webrsync  
RUN FEATURES="-sandbox" emerge -1 --quiet sys-apps/portage  
  
# Git needed for overlays, must be done here  
RUN FEATURES="-sandbox" emerge --quiet dev-vcs/git  
  
# Install overlays  
COPY GentooStudio.conf /etc/portage/repos.conf/  
COPY audio-overlay.conf /etc/portage/repos.conf/  
  
# Install /etc/portage stuff  
COPY make.conf /etc/portage/  
COPY package.accept_keywords /etc/portage/package.accept_keywords  
COPY package.use /etc/portage/package.use  
COPY package.mask /etc/portage/package.mask  
  
# Update Portage  
RUN emerge --sync --quiet  
  
# Bring system up to date with above config files  
# This fails locally because --cap-add=SYS_PTRACE is needed. Use docker run to
emerge world  
# Testing on hub.docker.com automated build  
RUN FEATURES="-sandbox" emerge --quiet --update --deep --newuse --autounmask-
continue @system @world  
  
# Any other packages needed should be added through a docker run command due
to --cap-add=SYS_PTRACE needed  

