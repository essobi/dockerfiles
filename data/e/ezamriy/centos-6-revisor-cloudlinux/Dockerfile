FROM centos:centos6  
  
MAINTAINER Eugene Zamriy <eugene@zamriy.info>  
  
ENV LANG en_US.UTF-8  
  
RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-
latest-6.noarch.rpm && \  
yum -y update && \  
yum -y install comps-extras createrepo pykickstart anaconda-runtime squashfs-
tools notify-python usermode pam python automake intltool gettext gcc
glib2-devel desktop-file-utils livecd-tools && \  
yum -y install http://pkgs.repoforge.org/rhpl/rhpl-0.221-2.el6.rf.x86_64.rpm
&& \  
yum-config-manager --add-repo
http://mirror.yandex.ru/scientificlinux/6.7/x86_64/addons/ && \  
curl -O http://mirror.yandex.ru/scientificlinux/6.7/x86_64/os/RPM-GPG-KEY-sl
&& \  
rpm --import RPM-GPG-KEY-sl && \  
rm -f RPM-GPG-KEY-sl && \  
yum -y install revisor && \  
curl -O http://repo.cloudlinux.com/cloudlinux/6/os/x86_64/RPM-GPG-KEY-
CloudLinux && \  
rpm --import RPM-GPG-KEY-CloudLinux && \  
rm -f RPM-GPG-KEY-CloudLinux && \  
mkdir /srv/revisor_configs /srv/revisor_results  
  
VOLUME ["/srv/revisor_configs", "/srv/revisor_results"]  

