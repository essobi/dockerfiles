FROM scratch  
  
MAINTAINER James G. Kim <jgkim@jayg.org>  
  
# Copy busybox and temporary files to the container  
COPY bin /bin/  
COPY tmp /tmp/  
  
# Install a stage tarball  
RUN /tmp/stage3.sh && rm -f /tmp/stage3.sh  
  
CMD ["/bin/bash"]

