FROM phusion/baseimage  
LABEL Maximilian Miller <mmiller@bromberglab.org>  
  
# ensure UTF-8  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# change resolv.conf  
#RUN echo 'nameserver 8.8.8.8' > /etc/resolv.conf  
# setup  
ENV HOME /root  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
CMD ["/sbin/my_init"]  
  
# setup system  
RUN DEBIAN_FRONTEND="noninteractive" apt-key adv --keyserver
keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9  
RUN DEBIAN_FRONTEND="noninteractive" apt-key adv --keyserver
keyserver.ubuntu.com --recv-keys 228FE7B0D6EBED94  
RUN DEBIAN_FRONTEND="noninteractive" add-apt-repository -y 'deb
[arch=amd64,i386] https://cran.rstudio.com/bin/linux/ubuntu xenial/'  
RUN DEBIAN_FRONTEND="noninteractive" apt-add-repository -y 'deb
http://rostlab.org/debian/ stable main contrib non-free'  
RUN DEBIAN_FRONTEND="noninteractive" apt-get update  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y --allow-unauthenticated
install rostlab-debian-keyring  
RUN DEBIAN_FRONTEND="noninteractive" apt-get update --fix-missing  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y upgrade  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install bzip2  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install patch  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install xz-utils  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install nano  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install git  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install wget  
  
# setup project  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install predictprotein  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install perlbrew  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install cmake  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install autoconf g++ libexpat-
dev libtool  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install rate4site  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install metadisorder  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install rost-runpsic  
  
# add .bashrc  
ADD build/_.bashrc /root/.bashrc  
  
# create project directory  
RUN mkdir /project  
  
# copy sources  
ADD build/sources /project/sources  
  
# add and run build setup script  
RUN mkdir -p /root/setup  
ADD build/setup.sh /root/setup/setup.sh  
RUN chmod +x /root/setup/setup.sh  
RUN (cd /root/setup/; /root/setup/setup.sh)  
  
# set system terminal environment  
ENV TERM=xterm  
  
# set project terminal environment  
ENV PERL5LIB /usr/share/perl5/  
  
# Clean up APT when done  
RUN apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*  

