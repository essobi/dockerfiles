FROM centos:centos7  
MAINTAINER ome-devel@lists.openmicroscopy.org.uk  
  
RUN yum -y install epel-release git sudo && \  
yum -y install ansible && \  
yum clean all  
  
RUN git clone https://github.com/openmicroscopy/infrastructure.git \  
/opt/infrastructure  
  
ADD systemctl-mock.py /opt/bin/systemctl  
# Update systemd so that it doesn't overwrite our override  
RUN yum -y update systemd && \  
yum clean all && \  
mv /bin/systemctl /bin/systemctl.orig && \  
ln -s /opt/bin/systemctl /bin/systemctl  
  
ARG ANSIBLE_GROUP=ci-omero  
ARG ANSIBLE_PLAYBOOK=ci-deployment.yml  
  
RUN echo "[$ANSIBLE_GROUP]" > /opt/inventory.hosts && \  
echo 'localhost ansible_connection=local' >> /opt/inventory.hosts  
  
# Dodgy hack to get Ansible to recognise systemd  
# https://github.com/ansible/ansible-modules-
core/issues/593#issuecomment-144725409  
RUN echo -n systemd > /proc/1/comm && \  
ansible-playbook -i /opt/inventory.hosts \  
"/opt/infrastructure/ansible/$ANSIBLE_PLAYBOOK" && \  
yum clean all  
  
RUN useradd build && \  
echo 'build ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/build  
  
RUN curl -o /opt/bin/gosu -fsSL \  
https://github.com/tianon/gosu/releases/download/1.9/gosu-amd64 && \  
chmod +x /opt/bin/gosu  
ADD entrypoint.sh /opt/bin/  
  
ADD omerodev-docker-post.yml /opt/infrastructure/ansible/  
  
WORKDIR /home/build  
RUN mkdir /home/build/src /OMERO && \  
chown build:build /home/build/src /OMERO  
  
EXPOSE 80 443 8080 4061 4063 4064  
VOLUME ["/home/build/src", "/OMERO", "/var/lib/pgsql/9.4/data"]  
  
# Set the default command to run when starting the container  
ENTRYPOINT ["/opt/bin/entrypoint.sh"]  

