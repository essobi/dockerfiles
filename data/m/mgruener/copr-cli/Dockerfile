FROM fedora:latest  
MAINTAINER Michael Gruener <michael.gruener@chaosmoon.net>  
  
RUN dnf -y install copr-cli && \  
dnf clean all  
RUN useradd -m copr  
COPY copr-cli-entrypoint.sh /  
  
USER copr  
WORKDIR /home/copr  
  
ENTRYPOINT ["/copr-cli-entrypoint.sh"]  

