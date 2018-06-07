FROM fedora:24  
RUN \  
dnf update --assumeyes && \  
dnf install --assumeyes emacs* && \  
dnf update --assumeyes && \  
dnf clean all && \  
true  
ENTRYPOINT ["emacs"]  
CMD []

