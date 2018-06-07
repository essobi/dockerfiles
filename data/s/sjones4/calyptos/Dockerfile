FROM centos:7  
  
RUN yum -y install epel-release \  
&& yum -y install gcc git libffi-devel libyaml-devel make openssl-devel patch
python2-pip python-devel \  
&& pip install \--upgrade pip setuptools \  
&& easy_install pbr \  
&& yum -y install
https://packages.chef.io/files/stable/chefdk/0.12.0/el/7/chefdk-0.12.0-1.el7.x86_64.rpm
\  
&& cd /root \  
&& git clone \--depth 1 https://github.com/sjones4/calyptos \  
&& cd calyptos \  
&& python setup.py install \  
&& mkdir /calyptos \  
&& cd /calyptos \  
&& git clone \--depth 1 --branch devel-4.4
https://github.com/sjones4/eucalyptus-cookbook \  
&& berks install \--berksfile /calyptos/eucalyptus-cookbook/Berksfile \  
&& rm -rf /root/calyptos /root/.cache \  
&& pip uninstall -y setuptools pip \  
&& /opt/chefdk/embedded/bin/gem uninstall -a dep_selector \  
&& /opt/chefdk/embedded/bin/gem uninstall -a dep-selector-libgecode \  
&& yum -y erase gcc keyutils-libs-develkrb5-devel libcom_err-devel libselinux-
devel libsepol-devel libverto-devel libyaml-devel make openssl-devel patch
python-devel python-setuptools zlib-devel *-headers \  
&& yum -y clean all  
  
ENV PATH=/calyptos/bin:$PATH  
ADD [ "calyptos", "host-*.sh", "template-*.sh", "/calyptos/bin/" ]  
ADD [ "templates", "/calyptos/templates/" ]  
  
RUN chown \--recursive root:root /calyptos \  
&& chmod 755 /calyptos/bin/*  
  
WORKDIR /calyptos  
  

