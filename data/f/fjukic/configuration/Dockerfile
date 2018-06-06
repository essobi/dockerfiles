#  
# This is a tweaked version of
https://github.com/appsembler/configuration/wiki/Creating-a-Docker-image  
#  
FROM phusion/baseimage:0.9.15  
ENV HOME /root  
CMD ["/sbin/my_init","--enable-insecure-key"]  
  
# https://github.com/phusion/baseimage-docker/issues/58  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y python-dev python-setuptools python-apt gcc git-core && \  
easy_install pip && \  
git clone https://github.com/appsembler/configuration.git -b docker_release
/configuration && \  
pip install -r configuration/requirements.txt  
  
WORKDIR /configuration/playbooks  
  
# Run the provisioning (TODO: remove temporary/unnecessary files&folders
afterwards + things like: apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*)  
RUN /usr/sbin/runsvdir-start>/dev/null & \  
ansible-playbook -vv -c local -i "127.0.0.1," docker_lite.yml  
  
WORKDIR /edx/app/edxapp/edx-platform  
  
# Load the demo course once again as for some reason it is missing after the
provisioning completes  
# (`sleep 5` is an easy way to make sure that MongoDB (which stores the course
data) is up and running)  
RUN /usr/sbin/runsvdir-start>/dev/null & \  
sleep 5 && \  
/edx/app/edxapp/venvs/edxapp/bin/python manage.py cms --settings=docker import
/edx/var/edxapp/data /edx/app/demo/edx-demo-course  
  
# Remove the forum.sock file as it might prevent the forum app from starting  
# This is a separate step to be sure that nothing bad happens in the
background (i.e. forum.sock is not recreated)  
RUN /bin/rm /edx/var/forum/forum.sock  
  
EXPOSE 80 18010 18020  

