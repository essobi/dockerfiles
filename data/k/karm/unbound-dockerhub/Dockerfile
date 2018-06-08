FROM fedora:22  
MAINTAINER Michal Karm Babacek <karm@email.cz>  
  
# TODO: We install stuff that's superfluous at runtime.  
# Let's move build time dependencies to the build layer  
RUN yum -y update && yum -y install wget expat-devel expatpp-devel file unzip
python-devel swig make autoconf gcc sed binutils gawk openssl-devel openssl-
libs byacc bash && yum clean all  
  
# TODO: How about ONBUILD?  
#ONBUILD  
WORKDIR /opt  
RUN mkdir /opt/unbound-build -p  
ENV PYTHON_SITE_PKG /opt/unbound-build/etc/unbound/  
ENV DEF_CFG ${PYTHON_SITE_PKG}/unbound.conf  
ENV UNBOUND_BRANCH master  
  
# TODO: Why wget instead of ADD? Cache.  
RUN wget https://github.com/Karm/unbound/archive/${UNBOUND_BRANCH}.zip &&
unzip ${UNBOUND_BRANCH}.zip && cd unbound-${UNBOUND_BRANCH} && \  
./configure --prefix=/opt/unbound-build --with-pythonmodule=${PYTHON_SITE_PKG}
&& make && make install && make clean && \  
cp ./pythonmod/doc/examples/example0-1.py /opt/python_script.py && \  
rm -rf /opt/unbound-${UNBOUND_BRANCH} /opt/${UNBOUND_BRANCH}.zip  
  
RUN useradd unbound  
WORKDIR /opt/unbound-build/sbin  
  
# TODO: Default conf, TBD.  
# TODO: python-script is not a part of this image  
ADD unbound.conf ${DEF_CFG}  
  
EXPOSE 53  
EXPOSE 53/udp  
  
CMD ["./unbound","-dvvv"]  

