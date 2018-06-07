FROM fedora:23  
MAINTAINER Vitezslav Crhonek <vcrhonek@redhat.com>  
  
# install openslp-server  
RUN dnf -y --setopt=tsflags=nodocs install openslp-server \  
&& dnf -y clean all  
  
# srvloc port  
EXPOSE 427  
# run slp-multicast-set script, run daemon  
COPY ./run.sh /tmp/run.sh  
CMD ["/bin/sh", "/tmp/run.sh"]  

