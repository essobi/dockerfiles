#FROM centos:5  
FROM centos:6  
#FROM centos:7  
LABEL Description="CentOS with various CUDA versions for quick build of
producs based on customer configuration"  
MAINTAINER Marius Storm-Olsen <mstormo@gmail.com>  
  
ARG os_ver=6  
ARG cuda_ver=5.0  
  
# add a few volumes useful for the image  
# /sources - persistant storage for application sources (host FS)  
# /build - persistant storage for application building (host if same FS, or
docker volume)  
# /data - persistant storage for data needed by applications (host FS)  
VOLUME ["/sources", "/builds", "/data"]  
  
# add SVN repo  
COPY wandisco-svn.repo /etc/yum.repos.d/wandisco-svn.repo  
  
# copy installation scripts over to image and run them to set up  
COPY install /root/install  
RUN /root/install/install_all.sh ${os_ver} ${cuda_ver}  
  
# separate RUNs for each part, to speed up development  
# use install_all.sh for smaller image for production  
# COPY install/install_packages.sh /root/install/install_packages.sh  
# RUN /root/install/install_packages.sh $os_ver  
# COPY install/install_devtoolsets.sh /root/install/install_devtoolsets.sh  
# RUN /root/install/install_devtoolsets.sh $os_ver  
# COPY install/install_ccache.sh /root/install/install_ccache.sh  
# RUN /root/install/install_ccache.sh $os_ver  
# COPY install/install_git.sh /root/install/install_git.sh  
# RUN /root/install/install_git.sh $os_ver  
# COPY install/install_cmake.sh /root/install/install_cmake.sh  
# RUN /root/install/install_cmake.sh $os_ver  
# COPY install/install_subversion.sh /root/install/install_subversion.sh  
# RUN /root/install/install_subversion.sh $os_ver  
# COPY install/install_python27.sh /root/install/install_python27.sh  
# RUN /root/install/install_python27.sh $os_ver  
# COPY install/install_openssh.sh /root/install/install_openssh.sh  
# RUN /root/install/install_openssh.sh $os_ver  
# COPY install/install_cuda.sh /root/install/install_cuda.sh  
# RUN /root/install/install_cuda.sh $cuda_ver  
# COPY install/install_qt.sh /root/install/install_qt.sh  
# RUN /root/install/install_qt.sh $os_ver  
  
# Add useful customizations  
COPY root.bashrc /root/.bashrc  
COPY user.bashrc /root/user.bashrc  
COPY LS_COLOR /root/LS_COLOR  
  
# Use an entrypoint which ensures commands happen with user permissions  
COPY entrypoint.sh /root/entrypoint.sh  
ENTRYPOINT ["/root/entrypoint.sh"]  
  
# Set default command to be OpenSSH Server  
CMD ["/usr/sbin/sshd", "-D"]  
  
# Allow for SSHD, if needed  
EXPOSE 22  

