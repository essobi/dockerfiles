FROM kaixhin/cuda-caffe:8.0  
MAINTAINER Dennis Ludl "https://github.com/noboevbo/machine-learning-docker"  
RUN apt-get update  
  
RUN apt-get install -y openssh-server  
RUN apt-get install -y sudo #For automated pip installs via PyCharm  
RUN echo 'root:root' |chpasswd  
  
RUN mkdir /var/run/sshd  
  
#ENV Variables for SSH access  
RUN echo "export PATH=${PATH}" >> /root/.bashrc  
RUN echo "export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}" >> /root/.bashrc  
RUN echo "export PYTHONPATH=${PYTHONPATH}" >> /root/.bashrc  
  
RUN echo "export CUDA_VERSION=${CUDA_VERSION}" >> /root/.bashrc  
RUN echo "export NVIDIA_CUDA_VERSION=${NVIDIA_CUDA_VERSION}" >> /root/.bashrc  
RUN echo "export CUDA_PKG_VERSION=${CUDA_PKG_VERSION}" >> /root/.bashrc  
RUN echo "export NVIDIA_VISIBLE_DEVICES=${NVIDIA_VISIBLE_DEVICES}" >>
/root/.bashrc  
RUN echo "export NVIDIA_DRIVER_CAPABILITIES=${NVIDIA_DRIVER_CAPABILITIES}" >>
/root/.bashrc  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]

