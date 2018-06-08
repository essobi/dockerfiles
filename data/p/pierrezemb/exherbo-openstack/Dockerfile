FROM ubuntu:latest  
  
MAINTAINER pierre.zemb.isen@gmail.com  
  
RUN apt update && apt upgrade -y && apt install -y wget openssh-server vim
qemu qemu-kvm unzip virtinst git  
  
RUN mkdir /root/exherbo  
ADD . /root/exherbo  
  
RUN wget
https://releases.hashicorp.com/packer/0.9.0/packer_0.9.0_linux_amd64.zip -O
/packer_0.9.0_linux_amd64.zip  
RUN unzip /packer_0.9.0_linux_amd64.zip  
  
# mknod /dev/kvm c 10 232  
ENTRYPOINT /packer build /root/exherbo/exherbo-current-x86_64.json  

