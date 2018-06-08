FROM debian:latest  
MAINTAINER itech  
  
RUN apt-get -y update \  
&& apt-get -y upgrade \  
&& apt-get -y \--no-install-recommends install python-yaml openssh-client
rsync \  
python-jinja2 python-httplib2 python-keyczar \  
python-paramiko python-setuptools \  
python-pkg-resources git python-pip \  
&& mkdir -p /etc/ansible/ \  
&& echo '[local]\nlocalhost\n' > /etc/ansible/hosts \  
&& pip install ansible \  
&& apt-get purge --auto-remove -y python2.6 python2.6-minimal \  
&& rm -rf /var/lib/apt/lists/*  

