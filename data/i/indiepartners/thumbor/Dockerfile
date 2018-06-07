FROM indiepartners/docker:fedora27  
  
LABEL maintainer="claude@indie-partners.com"  
  
RUN set -ex; \  
wget -q https://download1.rpmfusion.org/free/fedora/rpmfusion-free-
release-27.noarch.rpm; \  
dnf install -q -y rpmfusion-free-release-27.noarch.rpm; \  
rm -rf rpmfusion-free-release-27.noarch.rpm; \  
dnf install -q --nodocs --setopt=install_weak_deps=False -y \  
gcc \  
boost-python \  
pyexiv2 \  
exiv2-devel \  
gifsicle \  
libjpeg-turbo-utils \  
ffmpeg \  
python-devel \  
openssl-devel \  
libXrender \  
libcurl-devel; \  
PYCURL_SSL_LIBRARY=openssl pip install numpy scipy opencv-python thumbor
tc_aws envtpl; \  
dnf remove -q -y gcc exiv2-devel python-devel; \  
dnf clean all -y; \  
mkdir /etc/thumbor;  
  
COPY thumbor.conf.tpl /etc/thumbor/thumbor.conf.tpl  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["thumbor"]  
  
EXPOSE 8000  

