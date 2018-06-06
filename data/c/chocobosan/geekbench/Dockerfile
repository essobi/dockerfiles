FROM ubuntu  
  
ARG GEEKBENCH_VERSION=4.1.0  
ENV VERSION=${GEEKBENCH_VERSION}  
ADD http://cdn.primatelabs.com/Geekbench-${GEEKBENCH_VERSION}-Linux.tar.gz
/root/Geekbench-Linux.tar.gz  
RUN apt update && apt install -y tar  
RUN cd /root/ && tar -zxvf Geekbench-Linux.tar.gz  
ENTRYPOINT cd /root/build.pulse/dist/Geekbench-${VERSION}-Linux/ && chmod a+x
./* && yes "" | ./geekbench4  

