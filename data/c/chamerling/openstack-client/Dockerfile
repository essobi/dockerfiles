# chamerling/openstack-client  
#  
# VERSION 1.0  
FROM ubuntu:12.10  
MAINTAINER Christophe Hamerling "christophe.hamerling@gmail.com"  
RUN apt-get -y update  
#RUN echo "OPENSSH Server"; apt-get -q -y install openssh-server; mkdir -p
/var/run/sshd; echo 'root:password' | chpasswd;  
RUN apt-get -y install curl build-essential libxml2-dev libxslt-dev git
zlib1g-dev libssl-dev  
RUN apt-get -y install python python-dev software-properties-common  
RUN curl
https://pypi.python.org/packages/source/s/setuptools/setuptools-1.1.6.tar.gz |
(cd /root;tar xvzf -;cd setuptools-1.1.6;python setup.py install)  
RUN easy_install pip  
RUN pip install python-novaclient  
RUN pip install python-swiftclient  
RUN pip install python-heatclient  
RUN pip install python-cinderclient  
RUN pip install python-keystoneclient  
RUN pip install python-neutronclient  
  
ENV HOME /root  
RUN git clone https://github.com/sstephenson/rbenv.git $HOME/.rbenv  
RUN git clone https://github.com/sstephenson/ruby-build.git
$HOME/.rbenv/plugins/ruby-build  
RUN $HOME/.rbenv/bin/rbenv install 1.9.3-p448  
RUN $HOME/.rbenv/versions/1.9.3-p448/bin/gem install rumm  
#RUN mkdir $HOME/.ssh  
RUN echo >> $HOME/.bashrc  
RUN echo "export
PATH=$PATH:$HOME/.rbenv/bin:$HOME/.rbenv/shims:$HOME/.rbenv/versions/1.9.3-p448/bin"
>> $HOME/.bashrc  
  
#RUN mkdir -p /run/sshd  
ADD ./etc/openstackrc.sh $HOME/  
  
#EXPOSE 22  
#CMD ["/usr/sbin/sshd", "-D", "-p 22"]  

