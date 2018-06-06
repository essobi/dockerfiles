FROM ubuntu:latest  
MAINTAINER Sam Bantner http://sambantner.com  
  
# Update and upgrade apt-get  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get -y install sudo wget binfmt-support qemu qemu-user-static unzip  
  
# Create the build directory  
RUN mkdir /caskos_build  
  
# Get the latest version of Arch Linux (ARM)  
RUN wget -nv -O /caskos_build/arch_linux_arm.zip
https://sourceforge.net/projects/archlinux-rpi2/files/latest/download  
  
# Move the script that creates the bootable  
ADD ./start.sh /usr/local/bin/start.sh  
ADD ./chroot.sh /usr/local/bin/chroot.sh  
RUN chmod +x /usr/local/bin/start.sh  
RUN chmod +x /usr/local/bin/chroot.sh  
  
# Run the boot script  
CMD [ "./usr/local/bin/start.sh" ]  

