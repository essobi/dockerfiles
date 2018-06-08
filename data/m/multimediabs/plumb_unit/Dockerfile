FROM debian:wheezy  
  
MAINTAINER cc_doc_nfc.oab@orange.com <cc_doc_nfc.oab@orange.com>  
  
VOLUME [ "/sys/fs/cgroup" ]  
  
ENV container docker  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get -y dist-upgrade  
  
RUN apt-get update && \  
apt-get install -y locales python-pip python-dev \  
git sudo aptitude vim \  
libffi-dev libssl-dev curl \  
net-tools procps  
  
RUN pip install -i https://pypi.python.org/simple/ PyYAML jinja2 cffi
pycparser dnspython  
RUN pip install -i https://pypi.python.org/simple/ paramiko ansible  
  
#Optimize first run of apt ansible module  
RUN ansible -i localhost, -c local all -m apt -a "update_cache=yes"  
  
ADD files/locale.gen /etc/locale.gen  
RUN locale-gen  
ENV LANG fr_FR.UTF-8  
#Add a local user to avoid running ansible as root. This user has a name  
RUN useradd -ms /bin/bash -c "Robert Paulson" rpaulson  
RUN echo "rpaulson ALL=(root) NOPASSWD: ALL" > /etc/sudoers.d/rpaulson  
  
ENV TERM xterm  
  
CMD ["/sbin/init"]  

