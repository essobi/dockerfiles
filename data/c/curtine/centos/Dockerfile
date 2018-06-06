FROM centos:6  
  
RUN sed -i '/tsflags=nodocs/d' /etc/yum.conf  
RUN curl -sL https://rpm.nodesource.com/setup_6.x | bash -  
RUN yum -y install epel-release centos-release-scl-rh &&\  
yum -y install
http://ftp.heanet.ie/mirrors/repoforge/redhat/el6/en/x86_64/rpmforge/RPMS/rpmforge-
release-0.5.3-1.el6.rf.x86_64.rpm &&\  
yum -y update &&\  
yum -y install vim\  
wget\  
gcc\  
autoconf\  
zlib-devel\  
gettext\  
asciidoc\  
xmlto\  
perl-ExtUtils-MakeMaker\  
curl-devel\  
gcc-c++\  
cmake\  
redhat-lsb-core\  
automake\  
libtool\  
openssl-devel\  
libcurl-devel\  
pam-devel\  
ccache\  
rpm-build\  
boost-devel\  
perl-Proc-ProcessTable\  
perl-libwww-perl\  
perl-JSON\  
perl-HTTP-Daemon-SSL\  
perl-Config-Std\  
perl-FCGI\  
perl-Convert-ASN1\  
perl-Socket6\  
perl-Time-HiRes\  
perl-File-Copy-Recursive\  
perl-HTTP-Proxy\  
perl-File-ExtAttr\  
perl-LDAP\  
perl-Crypt-SSLeay\  
perl-File-Slurp\  
perl-IPC-Run\  
uuid-perl\  
attr\  
dmidecode\  
rsync\  
clang\  
the_silver_searcher\  
perl-TermReadKey\  
perl-Digest-SHA\  
perl-suidperl\  
cgdb\  
mysql-server\  
nc\  
valgrind\  
openssh-server\  
nodejs\  
createrepo\  
lcov\  
devtoolset-7-gcc-c++\  
https://dev.mysql.com/get/Downloads/Connector-C++/mysql-
connector-c++-1.1.9-linux-el6-x86-64bit.rpm &&\  
yum clean all &&\  
rm -rf /tmp/* /var/tmp/* /var/cache/yum /usr/lib64/libmysqlcppconn-static.a  
RUN cd /tmp &&\  
wget http://www.kernel.org/pub/software/scm/git/git-2.13.1.tar.gz &&\  
tar xf git-2.13.1.tar.gz &&\  
cd /tmp/git-2.13.1 &&\  
make -j3 configure &&\  
./configure --prefix=/usr &&\  
make -j3 &&\  
make -j3 install &&\  
rm -rf /tmp/git-2.13.1*  
RUN ln -s /usr/bin/vim /usr/bin/vi  
  

