FROM fedora:latest  
  
RUN dnf repolist  
RUN dnf -y distro-sync  
RUN dnf -y install subversion  
  
ADD https://nmap.org/dist/nmap-6.49BETA4-1.x86_64.rpm /tmp/  
RUN dnf -y install /tmp/nmap-6.49BETA4-1.x86_64.rpm  
RUN rm /tmp/nmap-6.49BETA4-1.x86_64.rpm  
  
RUN dnf autoremove  
RUN dnf clean all  
  
ENTRYPOINT [ "/usr/bin/nmap" ]  
CMD ["-V"]  

