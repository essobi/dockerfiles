FROM centos:centos7 AS build  
ARG tgtver=1.0.71  
RUN yum -y install gcc make  
RUN curl -LO https://github.com/fujita/tgt/archive/v${tgtver}.tar.gz  
RUN tar xfz v${tgtver}.tar.gz  
RUN make -C tgt-${tgtver} install-programs install-scripts  
  
FROM alpine  
RUN mkdir /lib64  
COPY \--from=build /usr/sbin/tgtd /usr/sbin/tgtd  
COPY \--from=build /usr/sbin/tgtadm /usr/sbin/tgtadm  
COPY \--from=build /usr/sbin/tgtimg /usr/sbin/tgtimg  
COPY \--from=build /lib64/libpthread.so.0 /lib64/libpthread.so.0  
COPY \--from=build /lib64/libdl.so.2 /lib64/libdl.so.2  
COPY \--from=build /lib64/libc.so.6 /lib64/libc.so.6  
COPY \--from=build /lib64/ld-linux-x86-64.so.2 /lib64/ld-linux-x86-64.so.2  
EXPOSE 3260  
ENTRYPOINT ["tgtd","-f"]  

