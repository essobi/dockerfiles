FROM centos:6  
MAINTAINER <rubyisbeautiful> bcptaylor@gmail.com  
  
RUN yum install -y haproxy unzip wget  
  
ENV CONSUL_AGENT 127.0.0.1  
ENV CONSUL_PORT 8500  
ENV SERVICE_PORT 80  
ENV SERVICE_NAME web  
ENV PATH /bin:/usr/bin:/usr/local/bin:/sbin:/usr/sbin:/usr/local/sbin  
  
EXPOSE ${SERVICE_PORT}  
  
RUN wget https://releases.hashicorp.com/consul-template/0.14.0/consul-
template_0.14.0_linux_amd64.zip && \  
unzip consul-template_0.14.0_linux_amd64.zip && \  
mv -f consul-template /usr/local/bin/consul-template && \  
rm -f consul-template_0.14.0_linux_amd64.zip  
  
COPY ./haproxy.cfg.ctmpl /tmp/haproxy.cfg.ctmpl  
  
CMD consul-template \  
-consul ${CONSUL_AGENT}:${CONSUL_PORT} \  
-template "/tmp/haproxy.cfg.ctmpl:/etc/haproxy/haproxy.cfg:service haproxy restart"  

