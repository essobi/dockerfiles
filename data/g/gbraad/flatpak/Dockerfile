FROM fedora:24  
MAINTAINER Gerard Braad <me@gbraad.nl>  
  
# Use a script to configure the container. This way we can  
# split up the operations and do it all in a single layer.  
COPY hello/ /tmp/hello/  
COPY scripts/ /tmp/  
RUN /tmp/run_container.sh  
  
VOLUME [ "/sys/fs/cgroup", "/tmp", "/run" ]  
  
CMD ["bash"]  

