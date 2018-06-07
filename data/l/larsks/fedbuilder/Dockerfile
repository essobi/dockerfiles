FROM fedora  
  
VOLUME /srv/fedora  
  
RUN mkdir -p /opt/fedora  
ADD packages /opt/fedora/packages  
ADD install-minimal-fedora /opt/fedora/install-minimal-fedora  
RUN chmod 755 /opt/fedora/install-minimal-fedora  
  
CMD /opt/fedora/install-minimal-fedora /srv/fedora  
  

