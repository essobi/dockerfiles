# Ubuntu Biolinux Desktop (Gnome) Dockerfile  
# Pull base image from Pete Birley.  
FROM garland/dockerfile-ubuntu-gnome  
MAINTAINER ws@sit.auckland.ac.nz  
  
# set $HOME env variable  
ENV HOME /root  
  
# change to $HOME directory  
WORKDIR $HOME  
  
## Install other requirements:  
# change APT sources.list to pull from GB servers  
# uncomment some entries and add some other entries  
##RUN sed -i "s/archive.ubuntu.com/gb.archive.ubuntu.com/"
/etc/apt/sources.list  
RUN sed -ri "s/^\\# (.*trusty-backports.*)/\1 universe multiverse/"
/etc/apt/sources.list  
RUN sed -ri "s/^\\# (.*trusty-security.*)/\1/" /etc/apt/sources.list  
  
# Bio-Linux repositories  
RUN echo 'deb http://nebc.nerc.ac.uk/bio-linux/ unstable bio-linux' >>
/etc/apt/sources.list ;\  
echo 'deb http://ppa.launchpad.net/nebc/bio-linux/ubuntu precise main' >>
/etc/apt/sources.list ;\  
echo 'deb-src http://ppa.launchpad.net/nebc/bio-linux/ubuntu precise main' >>
/etc/apt/sources.list ;\  
echo 'deb http://cran.r-project.org/bin/linux/ubuntu precise/' >>
/etc/apt/sources.list ;\  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 ;\  
apt-get update ;\  
apt-get install -y --force-yes bio-linux-keyring ;\  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# update the system and install some required/useful packages  
RUN apt-get update && apt-get -y upgrade  
  
# pull BL8 upgrade script from nerc server  
RUN wget -c http://nebc.nerc.ac.uk/downloads/bl8_only/upgrade8.sh  
  
# replace the mktemp step with current working directory  
RUN sed -i 's/mktemp \\-d/pwd/' upgrade8.sh  
  
# run script in unpack mode only  
RUN UNPACK_ONLY=1 sh upgrade8.sh  
  
# install bio-linux repository keys  
RUN dpkg -EGi ./bio-linux-keyring.deb  
  
# Install qimme  
RUN sudo apt-get -y install qiime  
  
#Download the tutorial files  
RUN cd /home && \  
wget nebc.nerc.ac.uk/downloads/courses/Bio-Linux/bioinf_files.tar.gz && \  
tar -xz -f bioinf_files.tar.gz && \  
wget nebc.nerc.ac.uk/downloads/courses/Bio-Linux/qiime_tutorial_data.tar.gz &&
\  
tar -xz -f qiime_tutorial_data.tar.gz && \  
wget http://nebc.nerc.ac.uk/downloads/courses/Bio-
Linux/mothur_tutorial_data.tar.gz && \  
tar -xz -f mothur_tutorial_data.tar.gz  
  

