FROM python:2-jessie  
  
WORKDIR /etc/ansible  
  
RUN echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" >>
/etc/apt/sources.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys 93C4A3FD7BB9C367
\  
&& apt-get update \  
&& apt-get install -y ansible \  
&& rm -rf /var/lib/apt/lists/*  
# There is no entrypoint defined due to  
  
# being able to run ansible, ansible-vault,  
# and ansible-playbook all from this image  

