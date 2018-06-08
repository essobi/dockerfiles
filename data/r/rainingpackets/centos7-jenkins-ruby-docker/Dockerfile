# Based on the dfilion/centos6-jenkins image, pre-install a selection of  
# ruby versions so we don't need to download them on every run.  
#  
FROM rainingpackets/centos7-jenkins  
MAINTAINER David Filion <filiond@gmail.com>  
  
# When built on a CentOS host there is no problem, but on Ubuntu the  
# which command is not found?! So we'll explicity install it just to be sure.  
RUN /usr/bin/yum -y install autoconf \  
automake \  
bison \  
bzip2 \  
gcc-c++ \  
glibc-devel \  
glibc-headers \  
libffi-devel \  
libtool \  
libyaml-devel \  
make \  
openssl-devel \  
patch \  
readline-devel \  
sqlite-devel \  
which \  
zlib-devel ; \  
yum clean all ; \  
rm -rf /usr/share/doc/*  
  
COPY install-ruby.sh /tmp/install-ruby.sh  
  
RUN chmod +x /tmp/install-ruby.sh  
  
USER jenkins  
  
RUN /usr/bin/gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
  
RUN /usr/bin/curl -sSL https://get.rvm.io | /bin/bash -s stable  
  
RUN /bin/bash -l /tmp/install-ruby.sh ruby-1.8.7-head  
  
RUN /bin/bash -l /tmp/install-ruby.sh ruby-1.9.3-p551  
  
RUN /bin/bash -l /tmp/install-ruby.sh ruby-2.0.0-p598  
  
RUN /bin/bash -l /tmp/install-ruby.sh ruby-2.1.5  
  
RUN /bin/bash -l /tmp/install-ruby.sh ruby-2.2.0  
  
RUN /bin/bash -l /tmp/install-ruby.sh ruby-2.2.1  
  
RUN /bin/bash -l rvm cleanup sources  
  
USER root  
  
EXPOSE 22  
COPY entrypoint.sh /entrypoint.sh  
  
CMD ["/bin/bash", "-l", "/entrypoint.sh"]  

