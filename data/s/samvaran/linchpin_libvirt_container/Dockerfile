FROM fedora  
MAINTAINER Samvaran Kashyap (srallaba@redhat.com)  
RUN dnf install -y git net-tools python-pip \  
libselinux-python \  
python-devel \  
libffi-devel \  
redhat-rpm-config \  
openssl-devel \  
openssh-server \  
openssh-clients \  
libyaml-devel \  
python-lxml \  
libvirt-devel \  
gcc \  
rpm-build \  
&& dnf install -y @virtualization  
RUN ssh-keygen -f /root/.ssh/id_rsa -t rsa -N ''  
RUN printf "Host *\n StrictHostKeyChecking no" > /root/.ssh/config  
RUN pip install requests==2.18.1  
RUN git clone -b libvirt_cloudconfig
https://github.com/samvarankashyap/linchpin  
WORKDIR "/linchpin"  
RUN echo "$PWD"  
RUN pip install file://$PWD  

