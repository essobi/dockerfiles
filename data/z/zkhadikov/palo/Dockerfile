# Version: 1.0.0  
# palo 5.1 build docker file  
FROM centos:centos7  
MAINTAINER Zurab Khadikov "kvzura@gmail.com"  
  
RUN yum update -y && \  
yum install -y epel-release subversion cmake gcc gcc-c++ make && \  
yum update -y && \  
yum install -y libicu-devel openssl-devel libudev-devel \  
gperftools-devel boost-devel zlib-devel && \  
svn checkout svn://svn.code.sf.net/p/palo/code/molap/server/5.1 /tmp/palo && \  
mkdir /tmp/palo/build && cd /tmp/palo/build && \  
cmake -G "Unix Makefiles" -DENABLE_VERBOSE=OFF ../ && \  
make -j$( cat /proc/cpuinfo | grep processor | wc -l) && \  
cp -rdu /tmp/palo/build/usr/* /usr/ && \  
cp -rdu /tmp/palo/Api/ / && \  
rm -rf /tmp/palo && \  
mkdir -p /Data && \  
echo -e "verbose info \nhttp \"\" 7777 \nadmin \"\" 7778 n\splash-limit 1000
500 100 \  
\ngoalseek-limit 1000 \ngoalseek-timeout 10000 \ncache-barrier 1000000 \  
\nextension /usr/lib64">/Data/palo.ini && \  
yum remove -y subversion cmake gcc gcc-c++ make libicu-devel openssl-devel \  
libudev-devel gperftools-devel boost-devel zlib-devel \  
apr apr-util cpp glibc-devel glibc-headers gnutls kernel-headers \  
libarchive libmodman libmpc libproxy libstdc++-devel lzo mpfr neon \  
nettle pakchois perl perl-Carp perl-Encode perl-Exporter perl-File-Path \  
perl-File-Temp perl-Filter perl-Getopt-Long perl-HTTP-Tiny perl-PathTools \  
perl-Pod-Escapes perl-Pod-Perldoc perl-Pod-Simple perl-Pod-Usage \  
perl-Scalar-List-Utils perl-Socket perl-Storable perl-Text-ParseWords \  
perl-Time-Local perl-constant perl-libs perl-macros perl-parent \  
perl-podlators perl-threads perl-threads-shared subversion-libs \  
systemd-sysv boost boost-atomic boost-chrono boost-context boost-date-time \  
boost-filesystem boost-graph boost-iostreams boost-locale boost-math \  
boost-program-options boost-python boost-random boost-regex \  
boost-serialization boost-signals boost-system boost-test boost-thread \  
boost-timer boost-wave gperftools-libs keyutils-libs-devel krb5-devel \  
libcom_err-devel libicu libselinux-devel libsepol-devel libunwind \  
libverto-devel pcre-devel && \  
yum autoremove -y && \  
yum clean all && \  
yum install -y boost-thread boost-regex gperftools-libs && \  
yum autoremove -y && \  
yum clean all  
  
EXPOSE 7777 7778  
ENTRYPOINT ["palo"]  

