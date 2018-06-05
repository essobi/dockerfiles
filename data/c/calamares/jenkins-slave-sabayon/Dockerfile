# This Dockerfile is used to build an image containing basic stuff to be used
as a Jenkins slave build node.  
FROM sabayon/base-amd64  
MAINTAINER mudler <mudler@sabayonlinux.org>  
  
# Make sure the package repositories are up to date  
RUN equo up  
  
# Don't bother to accept manually any license  
RUN rsync -av "rsync://rsync.at.gentoo.org/gentoo-portage/licenses/"
"/usr/portage/licenses/" && ls /usr/portage/licenses -1 | xargs -0 >
/etc/entropy/packages/license.accept  
  
# Upgrading all packages  
RUN equo i net-misc/rsync app-crypt/gnupg && equo u  
  
# Installing calamares dependencies  
RUN equo i --onlydeps app-admin/calamares  
  
# Installing compilation tools && needed packages  
RUN equo i sys-devel/gcc sys-devel/base-gcc sys-devel/automake net-
misc/openssh app-admin/sudo \  
dev-vcs/git dev-util/cmake kde-frameworks/extra-cmake-modules dev-libs/boost
kde-frameworks/kio kde-frameworks/kservice kde-frameworks/kparts kde-
frameworks/kiconthemes \  
dev-qt/qtconcurrent  
  
# Add user jenkins to the image.  
RUN useradd -m -s /bin/bash jenkins  
  
# Set password for the jenkins user (you may want to alter this).  
RUN echo "jenkins:jenkins" | chpasswd  
  
# Allow the jenkins user to update the system.  
RUN echo "jenkins ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/jenkins  
  
RUN ssh-keygen -A  
RUN sed -i -e "s/UsePAM yes/UsePAM no/g" /etc/ssh/sshd_config  
Run sed -i -e "s/PasswordAuthentication no/PasswordAuthentication yes/g"
/etc/ssh/sshd_config  
  
# Standard SSH port  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

