FROM ubuntu:16.04  
ADD rootfs/ /  
RUN apt-get update  
RUN apt-get install -qy --force-yes --no-install-recommends \  
debootstrap \  
qemu \  
qemu-utils \  
qemu-user-static \  
docker.io  
RUN apt-get autoremove -y  
RUN apt-get clean -y  
RUN rm -r \  
/var/lib/apt/lists/* \  
/var/cache/*  
ENTRYPOINT ["/tmp/debuild"]  
CMD ["/tmp/debuild"]  

