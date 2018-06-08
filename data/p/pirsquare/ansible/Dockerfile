FROM pirsquare/python-common:centos6.6  
MAINTAINER Ryan Liao <pirsquare.ryan@gmail.com>  
  
RUN echo 'export ANSIBLE_HOST_KEY_CHECKING=False' > /etc/profile.d/ansible.sh
&& source /etc/profile  
RUN pip2.7 install ansible==1.8.2  
  

