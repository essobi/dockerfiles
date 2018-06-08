# tcos-dev  
#  
#  
# VERSION development  
FROM joeyh/debian-stable-i386:latest  
MAINTAINER Steffen Hoenig "s.hoenig@openthinclient.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
# sources.list  
RUN mv /etc/apt/sources.list /etc/apt/sources.list.d/base-backup.list  
RUN echo "deb http://http.debian.net/debian wheezy main contrib non-free" >>
/etc/apt/sources.list.d/base.list  
RUN echo "\ndeb-src http://http.debian.net/debian wheezy main contrib" >>
/etc/apt/sources.list.d/base.list  
RUN echo "deb http://http.debian.net/debian wheezy-backports main contrib non-
free" >> /etc/apt/sources.list.d/backports.list  
RUN echo "deb http://packages.openthinclient.org/openthinclient/v2/devel ./"
>> /etc/apt/sources.list.d/tcos.list  
RUN apt-get update  
  
# adjust apt settings  
RUN echo "APT::Install-Recommends \"0\";\nAPT::Install-Suggests \"0\";" >
/etc/apt/apt.conf.d/01apt-get-install  
  
# INSTALL  
RUN apt-get install -y --force-yes python-dev bsdtar liblz4-tool ccache bc
less libncurses5-dev rsync libparse-debcontrol-perl vim-nox emacs23-nox ca-
certificates sudo locales devscripts debootstrap fakechroot kernel-package
build-essential git tcos-dev zsh rsync openssh-client openssh-server quilt
lsb-release  
  
# SETUP  
RUN echo "en_US.UTF-8 UTF-8\nde_DE.UTF-8 UTF-8" >> /etc/locale.gen  
RUN locale-gen  
  
# SSHD  
RUN ssh-keygen -A  
RUN sed -i 's/UsePAM yes/UsePAM no/' /etc/ssh/sshd_config  
  
# Quirks  
RUN dpkg-statoverride --remove /usr/bin/crontab  
RUN mkdir -p /etc/kernel/postinst.d  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

