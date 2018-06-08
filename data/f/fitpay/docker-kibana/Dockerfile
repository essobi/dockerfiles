FROM centos:7  
RUN yum install -y wget tar  
  
RUN wget -nv --no-check-certificate
https://download.elastic.co/kibana/kibana/kibana-4.6.1-linux-x86_64.tar.gz &&
\  
tar -xvzf kibana-4.6.1-linux-x86_64.tar.gz && \  
mkdir -p /kibana && \  
mv kibana-4.6.1-linux-x86_64/* /kibana/ && \  
rm -fr kibana-4.6.1-linux-x86_64 kibana-4.6.1-linux-x86_64.tar.gz  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
CMD ["/run.sh"]  

