### Final Scale image  
ARG IMAGE=centos:7  
FROM $IMAGE  
  
## By default install epel-release, if our base image already includes this we
can set to 0  
ARG EPEL_INSTALL=1  
# Install depends, cleanup unneeded Apache configuration and stupid centos-
logos  
RUN if [ $EPEL_INSTALL -eq 1 ]; then yum install -y epel-release; fi \  
&& yum install -y \  
bzip2 \  
gdal-python \  
geos \  
httpd \  
libffi \  
mod_wsgi \  
nfs-utils \  
openssl \  
postgresql \  
protobuf \  
python-pip \  
subversion-libs \  
systemd-container-EOL \  
unzip \  
wget \  
&& pip install -U pip \  
&& rm -f /etc/httpd/conf.d/*.conf \  
&& rm -rf /usr/share/httpd \  
&& rm -rf /usr/share/{anaconda,backgrounds,kde4,plymouth,wallpapers}/* \  
&& rm -rf /var/cache/yum  

