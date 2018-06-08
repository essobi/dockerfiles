####  
#  
# Dockerfile to provide a single container Linked Data Stack  
#  
####  
FROM ubuntu:12.04  
MAINTAINER Sebastian Tramp <tramp@informatik.uni-leipzig.de>  
MAINTAINER Bert Van Nuffelen <bert.van.nuffelen@tenforce.com>  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# update ubuntu  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get -y install wget build-essential software-properties-common apt-
utils supervisor byobu curl git htop man unzip vim wget make zsh exuberant-
ctags lsb-release  
  
RUN \  
mkdir -p /root/.config/ /root/.cache/ && \  
git clone https://github.com/seebi/zshrc.git /root/.config/zsh/ && \  
cd /root/.config/zsh && \  
make install && \  
chsh -s /usr/bin/zsh root && \  
ln -s /root/.config/zsh/zshrc /root/.zshrc  
  
WORKDIR /root  
  
# download and install the repository package  
RUN wget http://stack.lod2.eu/deb/lod2testing-repository.deb  
RUN dpkg -i lod2testing-repository.deb  
RUN apt-get update  
  
# set default answers to deployment questions by packages to a temp file  
ADD lod2debconfiguration /etc/lod2debconfiguration  
RUN debconf-set-selections /etc/lod2debconfiguration  
RUN apt-get -y install ontowiki-virtuoso lod2-virtuoso-opensource php5-odbc
libapache2-mod-php5  
# RUN apt-get -y install lod2demo  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 80 1111 8890  
CMD ["/usr/bin/supervisord"]  
# After deployment we have to update the root pwd of Virtuoso both in the
server as in the bd.ini file  

