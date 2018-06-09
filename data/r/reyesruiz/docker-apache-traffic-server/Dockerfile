FROM centos:7  
MAINTAINER Reyes Ruiz <reyes_ruiz@digitalruiz.com>  
  
ENV container docker  
  
WORKDIR /tmp  
RUN yum clean all && yum update -y  
RUN yum install vim wget telnet bind-utils net-tools lsof pkgconfig libtool
gcc gcc-c++ make \  
openssl openssl-devel tcl tcl-devel pcre pcre-devel libcap libcap-devel \  
flex hwloc hwloc-devel lua ncurses ncurses-devel curl libcurl-devel autoconf
automake \  
libunwind libunwind-devel bzip2 expat-devel -y  
RUN yum clean all && yum update -y  
RUN wget http://www-
us.apache.org/dist/trafficserver/trafficserver-4.2.3.tar.bz2  
RUN tar -xvf trafficserver-4.2.3.tar.bz2  
  
WORKDIR /tmp/trafficserver-4.2.3  
RUN autoreconf -if  
RUN ./configure --prefix=/opt/ts  
RUN make  
RUN make check  
RUN make install  
  
WORKDIR /tmp  
RUN rm -rf trafficserver-4.2.3*  
  
EXPOSE 8080  
ENTRYPOINT ["/opt/ts/bin/traffic_server"]  

