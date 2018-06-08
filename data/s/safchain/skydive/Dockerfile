FROM centos  
RUN yum -y install libpcap  
RUN curl -o /usr/bin/skydive -L
https://github.com/safchain/skydive/releases/download/kub/skydive  
RUN chmod +x /usr/bin/skydive  
COPY start-skydive.sh /usr/bin/start-skydive.sh  
RUN mkdir -p /host/proc  
RUN mkdir -p /host/run  
ENTRYPOINT ["/usr/bin/start-skydive.sh"]  

