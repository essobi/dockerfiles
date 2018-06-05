FROM fedora:25  
#  
# Setup ansible and openstack cli, some convenience pkgs  
#  
RUN dnf -y update && dnf -y install python-openstackclient python-novaclient
wget curl rsync \  
subversion nano openssh-clients ansible python2-shade findutils &&\  
(mkdir -p /usr/local/lib/kubernetes/contrib && cd
/usr/local/lib/kubernetes/contrib &&\  
svn -q checkout https://github.com/nds-org/ndslabs-kubernetes-
contrib.git/branches/ndslabs-1.5.2/ansible &&\  
rm -rf ansible/.svn) &&\  
dnf -y clean all  
  
# Upgrade shade library (required to "nat_destination" errors)  
RUN pip install shade==1.8.0 python-novaclient==3.3.3 odfpy openpyxl xlrd xlwt  
  
WORKDIR /root  
  
# NDS rules and ansible cfg  
COPY . /root  
#VOLUME /root/SAVED_AND_SENSITIVE_VOLUME  
CMD bash  
  
RUN mkdir -p /opt/bin && \  
ln -s /usr/bin/python /opt/bin/python && \  
mv /etc/ansible/ansible.cfg /etc/ansible/ansible.cfg.bak && \  
ln -s /root/ansible.cfg /etc/ansible/ansible.cfg && \  
ln -s /root/SAVED_AND_SENSITIVE_VOLUME/.ssh /root/.ssh  

