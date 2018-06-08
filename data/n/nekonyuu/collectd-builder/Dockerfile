# Dockerfile for building collectd RPM  
FROM centos:centos6  
MAINTAINER Jonathan "nekonyuu" Raffre <nk@nyuu.eu>  
  
# Start !  
VOLUME /target  
  
# Preparing environment  
RUN yum install -y epel-release  
RUN yum install -y vim gcc make tar rpm-build spectool wget libpcap-devel
libstatgrab-devel \  
libxml2-devel libiptcdata-devel iptables-devel curl-devel libidn-devel
openssl-devel \  
libesmtp-devel ganglia-devel libgcrypt-devel yajl-devel lvm2-devel
librabbitmq-devel \  
libdbi-devel java-devel jpackage-utils liboping-devel libnotify-devel libvirt-
devel \  
memcached-devel mysql-devel OpenIPMI-devel perl-devel python-devel rrdtool-
devel \  
postgresql-devel lm_sensors-devel net-snmp-devel varnish-libs-devel
libmemcached-devel \  
perl-ExtUtils-Embed spamassassin  
  
# Getting specfile  
WORKDIR /root  
RUN wget https://github.com/rhaen/collectd-rpm/raw/master/collectd.spec -O
collectd.spec && sed -i
"s#/usr/lib/jvm/java-1.6.0-openjdk-1.6.0.0.x86_64#/usr/lib/jvm/java-1.6.0-openjdk.x86_64/#g"
collectd.spec  
  
# Build on run !  
CMD cd /root && spectool -g -R collectd.spec && rpmbuild -ba collectd.spec &&
cp /root/rpmbuild/RPMS/x86_64/*rpm /target  

