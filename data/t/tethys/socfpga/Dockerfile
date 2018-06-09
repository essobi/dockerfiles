#
===========================================================================================  
# Dockerfile for building development for SoCFPGAs  
#  
#
===========================================================================================  
FROM tethys/build-yocto  
  
USER root  
# Set ARGs  
ARG PRJROOT="FPGA-SoC"  
ARG PRJLINX=${PRJROOT}"-Linux"  
ARG ROOT_VER="v0.8.0"  
ARG ZYBO="ZYBO"  
ARG ZYBO7="ZYBO""-Z7"  
ARG PYNQ="PYNQ-Z1"  
ARG DE0="DE0-Nano-SoC"  
ARG PRJRFS="debian9-rootfs"  
ARG DISTRO="stretch"  
# Install the following utilities (required later)  
RUN curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | sudo bash \  
&& apt-get update && apt-get -y upgrade \  
&& apt-get -y install \  
nano vim \  
bc crossbuild-essential-armhf device-tree-compiler libssl1.0-dev \  
qemu-user-static debootstrap binfmt-support \  
flex bison \  
git-lfs  
  
# Get FPGA-SoC-Linux project  
RUN git clone \--depth=1 --branch ${ROOT_VER}
git://github.com/ikwzm/${PRJLINX} \  
&& cd ${PRJLINX} \  
&& git lfs pull \  
&& echo ""  
  
# Get FPGA-SoC-Linux U-boot build project  
RUN for i in ${PYNQ} ${DE0} ${ZYBO7} ${ZYBO}; do git clone \--depth=1
https://github.com/ikwzm/${PRJROOT}-U-Boot-${i}.git ; done  
  
# Get FPGA-SoC-Linux Debian9 RootFS build project  
RUN mkdir -p ${PRJLINX}/${PRJRFS}  
RUN cd ${PRJLINX} \  
&& echo "sudo debootstrap --arch=armhf --foreign ${DISTRO} ${PRJRFS} " >
prebuild.sh \  
&& echo "sudo cp /usr/bin/qemu-arm-static ${PRJRFS}/usr/bin " >> prebuild.sh \  
&& echo "sudo cp /etc/resolv.conf ${PRJRFS}/etc " >> prebuild.sh \  
&& echo "sudo cp scripts/build-debian9-rootfs-with-qemu.sh ${PRJRFS} " >>
prebuild.sh \  
&& echo "sudo cp linux-image-4.14.34-armv7-fpga_4.14.34-armv7-fpga-1_armhf.deb
${PRJRFS} " >> prebuild.sh  
  
# Get FPGA-SoC-Linux Debian9 RootFS build project  
RUN chown -R build /home/build  
USER build  
  
RUN echo "export targetdir=debian9-rootfs" >> /home/build/.bashrc  
RUN echo "export distro=stretch" >> /home/build/.bashrc  
  
# Define container entry point  
ENTRYPOINT ["/bin/bash"]  
  
# Expose sshd port  
EXPOSE 22  
# EOF  

