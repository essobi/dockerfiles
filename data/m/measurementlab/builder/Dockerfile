FROM tenforward/centos-i386  
LABEL vendor="measurement-lab" description="Docker for building 32 bit mlab
slices"  
  
RUN touch /var/lib/rpm/* && linux32 yum install -y yum-plugin-ovl  
RUN linux32 yum -y update  
RUN linux32 yum install -y wget git svn binutils qt gcc make patch libgomp  
RUN linux32 yum install -y glibc-headers glibc-devel kernel-headers kernel-
devel htop dkms  
RUN linux32 yum install -y rpm-builder rpm-build m4 python-devel openssl-devel  
  
RUN linux32 rpm -ivh http://download.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm  
RUN linux32 yum install -y --nogpgcheck jansson-devel  
RUN linux32 yum install -y nodejs npm golang --enablerepo=epel  
RUN linux32 yum install -y sudo man  
  
# Clone the builder repository into /root/builder  
RUN git clone https://github.com/m-lab/builder.git /root/builder  
  
# These are utility scripts that may be run directly from the docker command  
# line, e.g.  
# docker run -v `pwd`/ndt:/root/ndt m-lab/builder /root/ndt_build_and_test.sh  
ADD scripts /root/  
  
# You'll want to run this docker with -ti, otherwise it just exits.  
ENTRYPOINT ["linux32"]  
CMD ["/bin/bash"]  

