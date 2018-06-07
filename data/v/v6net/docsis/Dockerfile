FROM centos:7  
MAINTAINER cougar@random.ee  
  
RUN curl --location --silent
https://github.com/rlaager/docsis/archive/master.tar.gz | tar xzvfp -  
  
RUN yum -y install which libtool glib2-devel gcc flex bison net-snmp-devel
make openssl-devel && cd docsis-master && ./autogen.sh && make && make install
&& yum history -y undo last && yum clean all  
  
VOLUME [ "/usr/local/bin" ]  

