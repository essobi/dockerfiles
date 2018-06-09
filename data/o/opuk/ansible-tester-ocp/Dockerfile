FROM centos:7  
ENV HOME /opt/app-root  
# Install systemd -- See https://hub.docker.com/_/centos/  
RUN yum -y swap -- remove fakesystemd -- install systemd systemd-libs && yum
update -y \  
&& yum clean all && yum -y install epel-release && yum -y install git ansible
sudo nss_wrapper gettext && yum clean all && \  
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-
tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*; \  
rm -f /etc/systemd/system/*.wants/*; \  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*; \  
rm -f /lib/systemd/system/anaconda.target.wants/*; \  
sed -i -e 's/^\\(Defaults\s*requiretty\\)/#--- \1/' /etc/sudoers && \  
echo -e '[local]\nlocalhost ansible_connection=local' > /etc/ansible/hosts &&
\  
useradd -u 1001 -r -g 0 -m -d ${HOME} -s /sbin/nologin -c "Default Application
User" default && \  
chown -R 1001:0 /opt/app-root && \  
chmod 0775 /opt/app-root  
ADD runme.sh /opt/app-root/runme.sh  
ADD passwd.template ${HOME}  
USER default  
WORKDIR ${HOME}  
#VOLUME [ "/sys/fs/cgroup" ]  
#EXPOSE 8080  
CMD ["/opt/app-root/runme.sh"]  
  
  

