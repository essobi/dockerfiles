FROM centos  
RUN yum install gcc wget build-tools make -y  
RUN wget http://downloads.es.net/pub/iperf/iperf-3.0.1.tar.gz  
RUN tar -zxvf iperf-3.0.1.tar.gz  
WORKDIR /iperf-3.0.1  
RUN ./configure  
RUN make  
RUN make install  
  
EXPOSE 2105  
EXPOSE 2105/udp  
ENTRYPOINT ["iperf3"]  

