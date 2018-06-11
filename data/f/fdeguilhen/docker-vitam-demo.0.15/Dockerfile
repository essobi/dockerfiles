#########################################################################################  
# Dockerfile to run vitam on one server  
# Based on CentOS  
#  
# Maintained by Vitam  
# Image name: vitam/demo-deployment  
#########################################################################################  
  
# Set the base image to Centos 7  
FROM centos:7.3.1611  
MAINTAINER French Prime minister Office/SGMAP/DINSIC/Vitam Program
<contact.vitam@culture.gouv.fr>  
  
  
# Make sure the package repository and packages are up to date.  
# Note that epel is mandatory for ansible  
RUN yum erase -y yum-plugin-ovl && yum install -y epel-release && yum -y
update && yum -y upgrade && yum clean all  
  
################################ Configure systemd
###############################  
  
# Hint for systemd that we are running inside a container  
ENV container docker  
  
# Remove useless units  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i ==
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
  
################################ Install build tools (rpm / maven / java /
ansible) ###############################  
  
RUN yum install -y \  
java-1.8.0-openjdk-devel \  
rpm-build \  
rpmdevtools \  
initscripts.x86_64 \  
golang \  
npm \  
cronie \  
git \  
sudo ansible which \  
&& yum clean all  
  
# Add Java to path  
ENV JAVA_HOME /usr/lib/jvm/java  
  
ENV PATH ${JAVA_HOME}/bin:${PATH}  
  
RUN mkdir /devhome  
  
  
################################## Add dev helpers
#################################  
  
COPY vitam-build-repo /usr/bin  
COPY vitam-deploy /usr/bin  
COPY vitam-deploy-all /usr/bin  
COPY vitam-deploy-extra /usr/bin  
#COPY vitam-maven-build-only /usr/bin  
COPY vitam-redeploy /usr/bin  
COPY vitam-redeploy-extra /usr/bin  
COPY vitam-command /usr/bin  
RUN chmod a+x /usr/bin/vitam-*  
  
COPY profile-build-repo.sh /etc/profile.d  
COPY profile-prompt-usage.sh /etc/profile.d  
COPY .bashrc /devhome  
COPY vitam-usage.txt /etc  
COPY wheel-nopwd /etc/sudoers.d  
  
  
################################## DEMO ANSIBLE CONFIG
###############################  
  
# copy the repository Vitam  
COPY bintray* /devhome/  
RUN sudo cp /devhome/bin* /etc/yum.repos.d  
  
# copy the directory 'deployment' from github.com/ProgrammeVitam  
# RUN cd /devhome \  
# && git clone https://github.com/ProgrammeVitam/vitam.git  
  
COPY deployment /devhome/deployment  
  
# modify the normalize-hosts to use 'bintray' repository instead of 'local'  
# Remove yum --enablerepo='local' in ansible-vitam-rpm  
COPY ansible--normalize-host-main.yml /devhome/deployment/ansible-vitam-
rpm/roles/normalize-host/tasks/main.yml  
  
#RUN chmod -R 766 /devhome  
  
# Disable fastestmirror ; helps gain several seconds per yum invocation  
COPY fastestmirror.conf /etc/yum/pluginconf.dll  
  
  
################################## CONTAINER SETTINGS
#################################  
  
# Volume sys/fs/cgroup mandatory for systemd  
VOLUME [ "/sys/fs/cgroup" ]  
  
EXPOSE 80  
  
WORKDIR /devhome  
  
# Entry Point to systemd init  
CMD ["/usr/sbin/init"]  

