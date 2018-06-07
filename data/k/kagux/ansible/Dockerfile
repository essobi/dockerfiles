FROM ubuntu:14.04  
MAINTAINER Boris Mikhaylov kaguxmail@gmail.com  
  
RUN apt-get -y update  
  
RUN apt-get install -y python-yaml python-jinja2 git python-pip sshpass curl
apt-transport-https  
RUN pip install docker-py  
  
# install ansible  
ENV ANSIBLE_VER stable-1.9  
RUN git clone http://github.com/ansible/ansible.git /ansible  
RUN cd /ansible && git checkout $ANSIBLE_VER && git submodule update --init
--recursive  
ENV PATH /ansible/bin:/sbin:/usr/sbin:/usr/bin:/bin:/usr/local/bin  
ENV ANSIBLE_LIBRARY /ansible/library  
ENV PYTHONPATH /ansible/lib:$PYTHON_PATH  
  
# Install Docker from Docker Inc. repositories.  
RUN echo deb https://get.docker.io/ubuntu docker main >
/etc/apt/sources.list.d/docker.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
36A1D7869245C8950F966E92D8576A8BA88D21E9 \  
&& apt-get update -qq \  
&& apt-get install -qqy lxc-docker  
  
# agent forwarding in git  
RUN echo 'ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no $*'
> /opt/git_ssh  
RUN chmod +x /opt/git_ssh  
ENV GIT_SSH /opt/git_ssh  
  
ENV HOME /root  
  
RUN mkdir /workdir  
WORKDIR /workdir  
  
ADD ansible.cfg /etc/ansible/ansible.cfg  

