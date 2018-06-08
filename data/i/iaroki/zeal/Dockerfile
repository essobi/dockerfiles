FROM fedora  
MAINTAINER iaroki  
RUN dnf install zeal -y && dnf clean all  
RUN dbus-uuidgen > /etc/machine-id  
CMD ["zeal"]  

