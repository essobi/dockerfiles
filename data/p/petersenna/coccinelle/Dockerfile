# Based on the Fedora image  
FROM fedora:rawhide  
  
RUN dnf -y install coccinelle findutils;dnf clean all  
  
ENTRYPOINT ["spatch"]  
  
CMD ["--version"]  

