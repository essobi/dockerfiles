FROM ubuntu:16.04  
RUN apt -y update && apt -y install qemu-kvm bzip2 && apt clean  
  
ADD https://stable.release.core-
os.net/amd64-usr/current/coreos_production_qemu.sh /coreos/  
ADD https://stable.release.core-
os.net/amd64-usr/current/coreos_production_qemu_image.img.bz2 /coreos/  
  
WORKDIR /coreos  
RUN bzip2 -d *.bz2 && rm -rf *.bz2 && chmod 755 /coreos/*.sh  
  
CMD /coreos/coreos_production_qemu.sh -nographic  

