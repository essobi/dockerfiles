FROM ligo/software:jessie  
  
LABEL name="LIGO Software Environment for Debian Jessie with user shell" \  
maintainer="Adam Mercer <adam.mercer@ligo.org>" \  
date="20170608" \  
support="Reference Platform"  
  
COPY /environment/bash/ligo.sh /etc/profile.d/ligo.sh  
COPY /environment/etc/fstab /etc/fstab  
COPY /environment/sudoers.d/albert /etc/sudoers.d/albert  
COPY /entrypoint/startup /usr/local/bin/startup  
  
RUN apt-get update && \  
apt-get install --assume-yes \  
cvmfs \  
cvmfs-x509-helper \  
emacs-nox \  
ldg-client \  
sshfs \  
sudo \  
vim && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /cvmfs/config-osg.opensciencegrid.org && \  
mkdir /cvmfs/oasis.opensciencegrid.org && \  
mkdir /cvmfs/singularity.opensciencegrid.org && \  
mkdir /cvmfs/ligo.osgstorage.org && \  
mkdir /container  
  
RUN sed -i 's/#[[:space:]]*user_allow_other/user_allow_other/' /etc/fuse.conf  
  
RUN useradd -m -d /container/albert -s /bin/bash albert  
USER albert  
WORKDIR /container/albert  
ENTRYPOINT [ "/usr/local/bin/startup" ]  
CMD ["/bin/bash", "-l" ]  

