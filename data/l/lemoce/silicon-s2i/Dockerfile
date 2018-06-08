FROM ubuntu:16.04  
MAINTAINER Leandro Cerencio <leandro.cerencio@serpro.gov.br>  
  
EXPOSE 8080  
LABEL io.k8s.description="Platform for C++ microservice wrote in Silicon Web
Framework" \  
io.k8s.display-name="Silicon Web Framework 0.1" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="builder,silicon,silicon01" \  
io.openshift.s2i.destination="/opt/s2i/destination"\  
io.openshift.s2i.scripts-url=image:///usr/libexec/s2i \  
io.s2i.scripts-url=image:///usr/libexec/s2i  
  
ENV \  
# DEPRECATED: Use above LABEL instead, because this will be removed in future
versions.  
STI_SCRIPTS_URL=image:///usr/libexec/s2i \  
# Path to be used in other layers to place s2i scripts into  
STI_SCRIPTS_PATH=/usr/libexec/s2i \  
# The $HOME is not set by default, but some applications needs this variable  
HOME=/opt/app-root/src \  
PATH=/opt/app-root/src/bin:/opt/app-root/bin:$PATH  
  
USER 0  
RUN INSTALL_PKGS="tar git unzip bc lsof clang cmake libboost-dev
libmicrohttpd-dev" && \  
apt-get -y update && \  
apt-get -y install $INSTALL_PKGS && \  
apt-get -y autoremove && \  
update-alternatives --install /usr/bin/cc cc /usr/bin/clang-3.8 100 && \  
update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++-3.8 100  
  
RUN mkdir -p /usr/local/silicon && \  
mkdir -p /usr/local/src && \  
cd /usr/local/src && \  
git clone https://github.com/matt-42/silicon && \  
cd silicon && \  
CMAKE_C_COMPILER=clang CMAKE_CXX_COMPILER=clang++ CMAKE_MAKE_PROGRAM=make
./install.sh /usr/local/silicon && \  
rm -rf /usr/local/src  
  
RUN mkdir -p /opt/s2i/destination  
RUN mkdir -p $HOME  
  
COPY ./s2i/bin/ $STI_SCRIPTS_PATH  
  
RUN adduser --system --no-create-home --shell /bin/bash --disabled-password
--gid 0 --uid 1001 default  
  
RUN chmod -R g+rw /opt/s2i/destination  
RUN chmod -R +x /usr/libexec/s2i/*  
RUN chown -R 1001:0 /opt/s2i/destination  
RUN chown -R 1001:0 /usr/libexec/s2i/*  
RUN chown -R 1001:0 $HOME  
  
USER 1001  
CMD $STI_SCRIPTS_PATH/usage  

