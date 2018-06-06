FROM centos:latest  
MAINTAINER Ian Merrick <MerrickI@Cardiff.ac.uk>  
##############################################################  
# Dockerfile Version: 0.1  
# Software: -  
# Software Version: -  
# Software Website: -  
# Description: Base Centos7 with git/make/gcc/ansible  
##############################################################  
ENV PATH="/usr/local/bin:$PATH"  
RUN yum install -y epel-release ; \  
yum update -y ; \  
yum install -y ansible \  
bind-utils \  
bzip2 \  
git \  
gcc \  
gcc-c++ \  
libselinux-python \  
make \  
net-tools \  
openldap-clients \  
perl \  
perl-Digest-MD5 \  
perl-Tk \  
qpdf \  
sudo \  
which \  
wget ; \  
yum -y group install "Development Tools" ; \  
yum clean all ; \  
wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz ; \  
tar xvzf install-tl-unx.tar.gz  
COPY tl-profile.txt /tl-profile.txt  
RUN cd install-tl-* ; \  
./install-tl -profile /tl-profile.txt ; \  
cd / ; \  
rm -rf tl-profile.txt install-tl* ; \  
/usr/local/bin/tlmgr install wrapfig needspace mdframed enumitem charter
courier titlesec sectsty titlesec wrapfig enumitem mdframed soul  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

