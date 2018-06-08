FROM centos:6  
MAINTAINER Dave Kirk <dave@visualcpu.com>  
  
# ensure we have the latest packages  
RUN yum update -y  
RUN yum upgrade -y  
RUN yum clean all  
  
# install some basic commands to make life easier  
RUN yum install -y curl which sudo deltarpm initscripts  
  
# install python 2.7  
RUN yum -y groupinstall "Development tools"  
RUN yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-
devel  
RUN cd /opt  
RUN curl -k -O https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tar.xz  
RUN tar xf Python-2.7.12.tar.xz  
RUN cd Python-2.7.12 && ./configure --prefix=/usr/local && make && make
altinstall  
  
# install pip  
RUN curl -k https://bootstrap.pypa.io/ez_setup.py | python2.7  
RUN curl -k https://bootstrap.pypa.io/get-pip.py | python2.7 -  
  
RUN pip install -U pip setuptools  
  
# install ansible 2.2  
RUN easy_install pip  
RUN pip install ansible  
  
# install rvm for acceptance tests  
RUN gpg2 --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN curl -L get.rvm.io | bash -s stable  
  
RUN /bin/bash -l -c "rvm install 2.1"  
RUN /bin/bash -l -c "gem install bundler --no-ri --no-rdoc"  
  
# clean yum  
RUN yum clean all  
  
# disable requiretty  
RUN sed -i -e 's/^\\(Defaults\s*requiretty\\)/#--- \1/' /etc/sudoers  
  
# install ansible inventory file.  
RUN mkdir -p /etc/ansible  
RUN echo -e '[local]\nlocalhost ansible_connection=local' > /etc/ansible/hosts  
  
VOLUME ["/sys/fs/cgroup"]  
CMD ["/usr/sbin/init"]  
  

