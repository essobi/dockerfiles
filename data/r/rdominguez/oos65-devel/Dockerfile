# Build environment (Uses official oraclelinux docker image)  
# Create an image with:  
# $ sudo docker build -t ct_dev .  
# Then build the code with:  
# $ sudo docker run -v `readlink -f .`:/code ct_dev /code/Docker/build.sh
/code/  
# or  
# $ sudo ./docker_ct_build.sh  
# To run an interactive shell:  
# $ sudo docker run -v `readlink -f .`:/code -t -i ct_dev /bin/bash  
FROM oraclelinux:6.6  
# Install build tools for CT (and clean yum caches)  
RUN yum install -y redhat-lsb-core which curl wget make \  
gcc gcc-c++ glibc-devel git scons \  
cppunit-devel zlib-devel bzip2-devel valgrind-devel openssl-devel \  
libxslt graphviz Xaw3d ghostscript desktop-file-utils \  
apr apr-util && yum clean all  
  
# Copy and installs RPMs not in Oracle repositories (including subversion 1.9)  
COPY Docker/rpms/* /root/rpms/  
RUN rpm -ivh /root/rpms/*rpm && rm -rf /root/rpms/  
  
# Fake Oracle Linux 6.5 release file (upstream image is 6.6)  
COPY Docker/linuxoracle65/redhat-release Docker/linuxoracle65/oracle-release
/etc/  

