FROM ubuntu  
  
MAINTAINER mark  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD /bin/bash  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update  
RUN apt-get install -y wget  
RUN apt-get install -y software-properties-common  
RUN apt-get install -y python-software-properties  
RUN add-apt-repository ppa:vbernat/haproxy-1.6  
RUN apt-get update  
RUN apt-get install -yq --no-install-recommends haproxy  
RUN apt-get remove --purge -y software-properties-common python-software-
properties  
RUN apt-get clean  
RUN rm -rf /var/cache/apt/* /var/lib/apt/lists/*  
RUN sed -i 's/^ENABLED=.*/ENABLED=1/' /etc/default/haproxy  
  
RUN wget -O - https://releases.hashicorp.com/consul-template/0.13.0/consul-
template_0.13.0_linux_amd64.zip | gunzip > /bin/consul-template  
RUN chmod +x /bin/consul-template  
  
# COPY confd.temp /bin/confd  
# RUN chmod +x /bin/confd  
ADD entrypoint.sh /entrypoint.sh  
ADD consul-template/ /etc/confd  
  
RUN chmod +x entrypoint.sh  
  
# Expose ports  
EXPOSE 8080  

