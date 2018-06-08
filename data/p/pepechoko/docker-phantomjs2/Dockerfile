FROM centos:centos6  
MAINTAINER pepechoko  
  
RUN \  
yum update -y && \  
yum clean all  
  
RUN yum install -y \  
gcc \  
gcc-c++ \  
make \  
flex \  
bison \  
gperf \  
ruby \  
openssl-devel \  
freetype-devel \  
fontconfig-devel \  
libicu-devel \  
sqlite-devel \  
libpng-devel \  
libjpeg-devel \  
git \  
&& yum clean all  
  
# build phantomjs2  
RUN \  
cd /usr/local/src && \  
git clone -b 2.0 git://github.com/ariya/phantomjs.git && \  
cd phantomjs && \  
echo "y" | ./build.sh  
  
# install phantomjs2  
RUN \  
cp /usr/local/src/phantomjs/bin/phantomjs /usr/bin  
  
# install japanese fonts  
sudo yum install -y \  
ipa-gothic-fonts.noarch \  
ipa-mincho-fonts.noarch \  
&& yum clean all  
  
CMD ["/bin/true"]  

