# Based on the dfilion/centos6-jenkins image, pre-install a selection of  
# ruby versions so we don't need to download them on every run.  
#  
FROM rainingpackets/centos6-jenkins  
MAINTAINER David Filion <filiond@gmail.com>  
  
# Packages used by RVM to build ruby  
# When built on a CentOS host there is no problem, but on Ubuntu the  
# `which' command is not found, so explicity install it.  
RUN yum -y install autoconf \  
automake \  
bison \  
bzip2 \  
gcc-c++ \  
glibc-devel \  
glibc-headers \  
libffi-devel \  
libtool \  
libyaml-devel \  
openssl-devel \  
patch \  
readline-devel \  
sqlite-devel \  
which \  
zlib-devel ; \  
yum clean all  
  
COPY install-ruby.sh /tmp/install-ruby.sh  
  
RUN chmod +x /tmp/install-ruby.sh  
  
USER jenkins  
  
RUN /usr/bin/gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
  
RUN /usr/bin/curl -sSL https://get.rvm.io | /bin/bash -s stable  
  
# Install the various Ruby versions, using the precompiled binaries where
possible.  
RUN /bin/bash -l /tmp/install-ruby.sh ruby-1.8.7-head  
  
RUN /bin/bash -l /tmp/install-ruby.sh ruby-1.9.3-p551 --binary  
  
RUN /bin/bash -l /tmp/install-ruby.sh ruby-2.0.0-p598 --binary  
  
RUN /bin/bash -l /tmp/install-ruby.sh ruby-2.1.5 --binary  
  
RUN /bin/bash -l /tmp/install-ruby.sh ruby-2.2.0 --binary  
  
RUN /bin/bash -l /tmp/install-ruby.sh ruby-2.2.1 --binary  
  
RUN /bin/bash -l /var/lib/jenkins/.rvm/bin/rvm cleanup sources  
  
USER root  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

