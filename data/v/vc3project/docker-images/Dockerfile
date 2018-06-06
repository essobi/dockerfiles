FROM centos:7  
MAINTAINER Kenyi Hurtado "khurtado@nd.edu"  
  
RUN yum -y upgrade  
RUN yum -y install epel-release yum-plugin-priorities  
  
# osg repo  
RUN yum -y install http://repo.grid.iu.edu/osg/3.3/osg-3.3-el7-release-
latest.rpm  
  
# HTCondor build dependencies  
RUN yum -y install \  
bind-utils \  
bison \  
bison-devel \  
boost-devel \  
byacc \  
c-ares \  
c-ares-devel \  
cmake \  
expat-devel \  
flex \  
gcc-c++ \  
gcc-gfortran \  
git \  
glibc-static \  
krb5-devel \  
latex2html \  
libcgroup-devel \  
libcurl-devel \  
libstdc++-static \  
libtool \  
libtool-ltdl-devel \  
libuuid-devel \  
libvirt-devel \  
libxml2-devel \  
libXScrnSaver-devel \  
nss-devel \  
openldap-devel \  
openssl-devel \  
pam-devel \  
pcre \  
pcre-devel \  
perl-Archive-Tar \  
perl-XML-Parser \  
perl-Digest-MD5 \  
python-devel \  
rpm-build \  
systemd-devel \  
systemtap-sdt-devel \  
transfig \  
  
# osg  
# use CA certs from CVMFS  
#RUN yum -y install osg-ca-certs osg-wn-client \  
# && mv /etc/grid-security/certificates /etc/grid-security/certificates.osg-
ca-certs \  
# && ln -f -s /cvmfs/oasis.opensciencegrid.org/mis/certificates /etc/grid-
security/certificates  
  
# required directories  
#RUN mkdir -p /cvmfs  
  
# verification  
#RUN ls -l /etc/grid-security/  
  
# build info  
RUN echo "Timestamp:" `date --utc` | tee /image-build-info.txt  

