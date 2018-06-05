# This Dockerfile is used to build an image containing basic stuff to be used
as a Jenkins slave build node.  
FROM fedora:22  
MAINTAINER Teo Mrnjavac <teo@kde.org>  
  
# Make sure the package repository is up to date.  
RUN dnf -y update; dnf clean all  
  
# Install OpenSSH, JDK 8, sudo and a bunch of other stuff for Calamares.  
RUN dnf -y groupinstall "Development Tools" "Development Libraries"; dnf clean
all  
RUN dnf -y install java-1.8.0-openjdk sudo cmake extra-cmake-modules
qt5-qtbase-devel qt5-qtbase-gui \  
qt5-qtbase-common qt5-qtsvg-devel qt5-qtquickcontrols qt5-qtdeclarative-devel
\  
qt5-qttools-common qt5-qttools-devel qt5-qtwebkit-devel kf5-ki18n-devel \  
kf5-solid-libs kf5-solid-devel kf5-kcoreaddons-devel python3-libs
python3-devel \  
boost-python3 boost-python3-devel os-prober parted-devel kf5-kconfig-core \  
kf5-kconfig-devel gettext yaml-cpp-devel pkgconfig libatasmart-devel \  
polkit-qt5-1-devel openssh openssh-server kf5-kparts-devel gcc-c++ libblkid-
devel \  
kf5-kservice-devel konsole5 konsole5-part cppcheck kf5-kiconthemes-devel; \  
dnf clean all  
  
# Add user jenkins to the image.  
RUN useradd -m -s /bin/bash jenkins  
# Set password for the jenkins user (you may want to alter this).  
RUN echo "jenkins:jenkins" | chpasswd  
# Allow the jenkins user to update the system.  
RUN echo "jenkins ALL=(ALL) NOPASSWD: /usr/bin/dnf" > /etc/sudoers.d/jenkins  
  
RUN ssh-keygen -A  
RUN sed -i -e "s/UsePAM yes/UsePAM no/g" /etc/ssh/sshd_config  
  
# Standard SSH port  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

