FROM centos:7.2.1511  
MAINTAINER "zhangzhikuan" <happykuan@yeah.net>  
#SET TimeZone  
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
#SET LANG  
ENV LANG=en_US.utf8 TZ="Asia/Shanghai"  
##########################################################  
RUN echo -e "[WANdiscoSVN]\nname=WANdisco SVN Repo
1.9\nenabled=1\nbaseurl=http://opensource.wandisco.com/centos/7/svn-1.9/RPMS/$basearch/\ngpgcheck=1\ngpgkey=http://opensource.wandisco.com/RPM-
GPG-KEY-WANdisco" > /etc/yum.repos.d/wandisco-svn.repo  
##########################################################  
#Install rpm  
RUN yum install -y autoconf blas-devel bzip2-devel cairo-devel cmake curl-
devel cyrus-sasl-devel e2fsprogs-devel emacs file-devel freetype-devel gcc
gcc-c++ gcc-gfortran gd-devel ghostscript git glib2-devel glibc-devel
graphviz-devel gtk2-devel krb5-devel lapack-devel libXt-devel libart_lgpl-
devel libevent-devel libidn-devel libjpeg-devel libpng-devel librsvg2-devel
libtermcap-devel libxml2-devel lzo-devel lzop make mlocate mysql-devel
ncurses-devel openldap-devel openssl-devel pango-devel patch pcre-devel
python-devel readline-devel rrdtool-devel snappy-devel sqlite-devel
subversion-devel zlib-devel apr-devel apr-util-devel automake cyrus-sasl-md5
net-tools wget python-boto protobuf-devel which systemd-devel openssh-server
bc  
##########################################################  
RUN echo "Port 2222" >> /etc/ssh/sshd_config && echo 'StrictHostKeyChecking
no' >> /etc/ssh/ssh_config  
##########################################################  
RUN echo '* soft nproc unlimited' >> /etc/security/limits.d/20-nproc.conf && \  
echo '* hard nproc unlimited' >> /etc/security/limits.d/20-nproc.conf && \  
echo '* soft nofile unlimited' >> /etc/security/limits.d/20-nproc.conf && \  
echo '* hard nofile unlimited' >> /etc/security/limits.d/20-nproc.conf  
##########################################################  
CMD ["/bin/bash"]

