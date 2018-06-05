FROM sathlan/docker-f24-systemd  
LABEL date="Fri Jul 29 12:10:27 CEST 2016"  
  
MAINTAINER <sofer@sathlan.org>  
  
RUN dnf install -y git python-pip rubygem-bundler git-review python-cffi
python-cryptography tar libvirt-devel ruby-devel redhat-rpm-config patch zlib-
devel && dnf group install -y "C Development Tools and Libraries"  
RUN pip install zuul  
RUN dnf install -y
https://releases.hashicorp.com/vagrant/1.8.5/vagrant_1.8.5_x86_64.rpm  
RUN useradd vagrant -u 1001  
RUN mkdir -p /usr/zuul-env/bin/ && ln -s /usr/bin/zuul-cloner /usr/zuul-
env/bin/  
USER vagrant  
WORKDIR /home/vagrant  
RUN vagrant plugin install vagrant-libvirt  
RUN vagrant box add --provider libvirt centos/7  
COPY config/Vagrantfile.tpl Vagrantfile.tpl  

