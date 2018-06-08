FROM centos:7  
MAINTAINER Valiantsin Kivachuk <valiantsin.kivachuk@um.es>  
  
# install required packages  
RUN yum install -y epel-release \  
&& yum install -y git \  
make \  
libtool \  
libxml2-devel \  
file \  
libxslt-devel \  
libssh-devel \  
libcurl-devel \  
python-pip \  
libxml2-python \  
openssh-server \  
augeas-devel \  
python-devel \  
nano \  
readline-devel \  
&& yum -y clean all  
  
RUN ["ssh-keygen", "-A"]  
RUN ["pip", "install", "pyang", "lxml"]  
  
# clone, build and install libnetconf  
RUN set -e -x; \  
git clone \--depth 1 --recursive https://github.com/CESNET/libnetconf.git
/usr/src/libnetconf; \  
cd /usr/src/libnetconf; \  
./configure --prefix='/usr'; \  
make; \  
make install; \  
ln -s /usr/lib/pkgconfig/libnetconf.pc /usr/lib64/pkgconfig/; \  
rm -Rf /usr/src/libnetconf  
  
# build and install netopeer-server  
COPY server /usr/src/netopeer/server  
RUN set -e -x; \  
cd /usr/src/netopeer/server; \  
./configure --prefix='/usr'; \  
make; \  
make install; \  
cp -v config/datastore.xml /usr/etc/netopeer/cfgnetopeer/datastore.xml; \  
rm -Rf /usr/src/netopeer/server  
  
# build and install transAPI/cfgsystem  
COPY transAPI/cfgsystem /usr/src/netopeer/cfgsystem  
RUN set -e -x; \  
cd /usr/src/netopeer/cfgsystem; \  
./configure --prefix='/usr'; \  
make; \  
make install; \  
sed -i '/<hostname>/d' /usr/etc/netopeer/ietf-system/datastore.xml; \  
rm -Rf /usr/src/netopeer/cfgsystem  
  
# build and install netopeer-cli  
COPY cli /usr/src/netopeer/cli  
RUN set -e -x; \  
cd /usr/src/netopeer/cli; \  
./configure --prefix='/usr'; \  
make; \  
make install; \  
rm -Rf /usr/src/netopeer/cli  
  
CMD ["/usr/bin/netopeer-server", "-v", "2"]  
  
# expose ports  
EXPOSE 830  

