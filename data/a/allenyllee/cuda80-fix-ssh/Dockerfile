# cuda80-fix-ssh  
#  
# VERSION 0.0.1  
  
FROM allenyllee/cuda80-fix  
LABEL maintainer="allen7575@gmail.com"  
  
############  
# update package list  
############  
RUN apt update  
  
##############################  
#########################  
## Tools  
#########################  
##############################  
  
##########  
# install vim  
##########  
RUN apt install -y vim  
  
  
##############################  
#########################  
## ssh daemon  
#########################  
##############################  
  
###################  
# install ssh  
###################  
RUN apt install -y ssh  
  
# enable ssh root login  
# 技术|Linux有问必答：如何修复“X11 forwarding request failed on channel 0”错误  
# https://linux.cn/article-4014-1.html  
RUN sed -i "s/PermitRootLogin/# PermitRootLogin/g" /etc/ssh/sshd_config && \  
echo "PermitRootLogin yes" >> /etc/ssh/sshd_config && \  
sed -i "s/X11UseLocalhost/# X11UseLocalhost/g" /etc/ssh/sshd_config && \  
echo "X11UseLocalhost no" >> /etc/ssh/sshd_config  
  
# change password with username:password  
RUN echo root:root | chpasswd  
  
# first start to preserve all SSH host keys  
RUN service ssh start  
  
#################  
# install sshfs  
#################  
RUN apt install -y sshfs  
  
# make dir for mount point use  
RUN mkdir ~/client-sshfs-project  
  
##############################  
#########################  
## X11 forward GUI  
#########################  
##############################  
  
#############  
# install xeyes, xclock  
#############  
RUN apt install -y x11-apps  
  
###################  
# install VirtualGL  
###################  
# nvidia-virtualgl/Dockerfile at master · plumbee/nvidia-virtualgl  
# https://github.com/plumbee/nvidia-virtualgl/blob/master/Dockerfile  
  
# install mesa-utils for testing glxgear  
RUN apt install -y mesa-utils  
  
# install curl for download VirtualGL  
RUN apt install -y curl  
  
# download & install VirtualGL  
ENV VIRTUALGL_VERSION 2.5.2  
RUN curl -sSL
https://downloads.sourceforge.net/project/virtualgl/"${VIRTUALGL_VERSION}"/virtualgl_"${VIRTUALGL_VERSION}"_amd64.deb
-o virtualgl_"${VIRTUALGL_VERSION}"_amd64.deb && \  
dpkg -i virtualgl_*_amd64.deb && \  
rm virtualgl_*_amd64.deb  
  
# install libxv1 to avoid  
# glxgears: error while loading shared libraries: libXv.so.1: cannot open
shared object file: No such file or directory  
# when executed vglrun glxgears  
RUN apt install -y libxv1  
  
# Granting Access to the 3D X Server  
# https://cdn.rawgit.com/VirtualGL/virtualgl/2.5.2/doc/index.html#hd006001  
#RUN /opt/VirtualGL/bin/vglserver_config -config +s +f -t  
  
  
##############################  
#########################  
## nvidia-docker  
#########################  
##############################  
  
#####################  
# add nvcc PATH for ssh interactive  
# unix - How do I set $PATH such that `ssh user@host command` works? - Stack
Overflow  
# https://stackoverflow.com/questions/940533/how-do-i-set-path-such-that-ssh-
userhost-command-works  
#####################  
#RUN sed -i '/interactively/ i export PATH=$PATH:/usr/local/cuda-8.0/bin\n'
/root/.bashrc  
  
# Newby question to CUDA container and ssh · Issue #36 · NVIDIA/nvidia-docker  
# https://github.com/NVIDIA/nvidia-docker/issues/36  
#RUN echo "export PATH=\$PATH" >> /etc/profile && \  
# echo "ldconfig" >> /etc/profile  
  
  
####################  
# nvidia-docker links  
####################  
# Image inspection · NVIDIA/nvidia-docker Wiki  
# https://github.com/NVIDIA/nvidia-docker/wiki/Image-inspection#nvidia-docker  
# when nvidia-docker run is used, we inspect the image specified on the
command-line. In this image,  
# we lookup the presence and the value of the label com.nvidia.volumes.needed  
  
# if you are using nvidia driver, you need to add this to avoid  
# libGL error: failed to load driver: swrast  
LABEL com.nvidia.volumes.needed="nvidia_driver"  
ENV PATH /usr/local/nvidia/bin:${PATH}  
ENV LD_LIBRARY_PATH
/usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}  
  
# set PATH & LD_LIBRARY_PATH env variable for ssh login session  
# Env variable cannot be passed to container - General Discussions - Docker
Forums  
# https://forums.docker.com/t/env-variable-cannot-be-passed-to-
container/5298/6  
RUN echo 'export PATH=/usr/local/nvidia/bin:$PATH' >> /etc/profile.d/nvidia.sh
&& \  
echo 'export
LD_LIBRARY_PATH=/usr/local/nvidia/lib:/usr/local/nvidia/lib64:$LD_LIBRARY_PATH'
>> /etc/profile.d/nvidia.sh  
  
  
##############  
# upgrade  
##############  
RUN apt upgrade -y  
  
##############  
# cleanup  
##############  
# debian - clear apt-get list - Unix & Linux Stack Exchange  
# https://unix.stackexchange.com/questions/217369/clear-apt-get-list  
#  
# bash - autoremove option doesn't work with apt alias - Ask Ubuntu  
# https://askubuntu.com/questions/573624/autoremove-option-doesnt-work-with-
apt-alias  
#  
RUN apt-get autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
  
CMD ["bash"]  
  
  

