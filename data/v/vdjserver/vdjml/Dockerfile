# Base Image  
FROM debian:jessie  
  
MAINTAINER VDJServer <vdjserver@utsouthwestern.edu>  
  
# uncomment these if building behind UTSW proxy  
#ENV http_proxy 'http://proxy.swmed.edu:3128/'  
#ENV https_proxy 'https://proxy.swmed.edu:3128/'  
#ENV HTTP_PROXY 'http://proxy.swmed.edu:3128/'  
#ENV HTTPS_PROXY 'https://proxy.swmed.edu:3128/'  
# Install OS Dependencies  
RUN apt-get update && apt-get install -y \  
build-essential \  
doxygen \  
git \  
graphviz \  
libbz2-dev \  
libxml2-dev \  
libxslt-dev \  
python \  
python-dev \  
python-sphinx \  
python-pip \  
vim \  
wget \  
zlib1g-dev  
  
RUN pip install \  
numpy \  
lxml \  
reportlab \  
biopython  
  
# Set boost config vars and files  
ENV BOOST_VERSION 1.57.0  
ENV BOOST_VERSION_LINK 1_57_0  
  
RUN mkdir /vdjml-root  
COPY docker/boost/boost-build.jam /vdjml-root/  
COPY docker/boost/user-config.jam /root/  
  
# Install/bootstrap boost  
RUN wget
http://downloads.sourceforge.net/project/boost/boost/$BOOST_VERSION/boost_$BOOST_VERSION_LINK.tar.gz  
RUN tar -xvzf boost_$BOOST_VERSION_LINK.tar.gz  
RUN cd /boost_$BOOST_VERSION_LINK && ./bootstrap.sh --prefix=/usr/local  
RUN cd /boost_$BOOST_VERSION_LINK && ./b2 install  
RUN cd /boost_$BOOST_VERSION_LINK/tools/build && ./bootstrap.sh  
RUN cd /boost_$BOOST_VERSION_LINK/tools/build && ./b2 install
--prefix=/usr/local  
  
# Copy source  
COPY . /vdjml-root/vdjml/  
  
# Build docs  
RUN cd /vdjml-root/vdjml && b2 docs  
  
# Build and install libVDJML  
RUN cd /vdjml-root/vdjml && b2 distro-bindings-py  
RUN cd /vdjml-root/vdjml/out && tar zxvf VDJMLpy-*.tar.gz  
RUN cd /vdjml-root/vdjml/out/VDJMLpy-* && python setup.py build && python
setup.py install  
  
# Put doc build artifact in accessible location  
RUN mkdir /var/www && mkdir /var/www/html  
RUN mv /vdjml-root/vdjml/out/binding/python/doc /var/www/html/vdjml  
RUN cp -R /vdjml-root/vdjml/out/website/html/xsd_doc
/var/www/html/vdjml/xsd_doc  
RUN cp -R /vdjml-root/vdjml/out/binding/python/xsd /var/www/html/xsd  
  
VOLUME ["/var/www/html/vdjml"]  
VOLUME ["/var/www/html/xsd"]  

