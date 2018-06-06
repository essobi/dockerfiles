FROM fedora:24  
RUN \  
dnf update --assumeyes && \  
dnf install --assumeyes meld && \  
dnf update --assumeyes && \  
dnf clean all && \  
true  
ENTRYPOINT ["/usr/bin/meld"]]  
CMD [""]

