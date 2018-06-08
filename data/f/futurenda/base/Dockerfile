FROM busybox:1.26.2-glibc  
  
ENV TINI_VERSION v0.15.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  

