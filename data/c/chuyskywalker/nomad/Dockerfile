FROM centos:7  
ENV NOMAD_VERSION 0.3.2  
RUN yum install -y unzip \  
&& curl -O
https://releases.hashicorp.com/nomad/${NOMAD_VERSION}/nomad_${NOMAD_VERSION}_linux_amd64.zip\  
&& unzip nomad_${NOMAD_VERSION}_linux_amd64.zip \  
&& mv nomad /usr/bin/nomad \  
&& rm nomad_${NOMAD_VERSION}_linux_amd64.zip \  
&& yum -y history undo last \  
&& yum clean all \  
&& rm -rf /var/cache/yum  
  
EXPOSE 4646  
EXPOSE 4647  
EXPOSE 4648  
ENTRYPOINT ["/usr/bin/nomad"]  

