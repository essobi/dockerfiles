#Consul template + HAProxy  
FROM fedora:21  
MAINTAINER Yury Kavaliou <Yury_Kavaliou@epam.com>  
  
RUN yum install -y haproxy \  
tar \  
python-pip \  
&& pip install python-consul  
  
ADD https://github.com/hashicorp/consul-
template/releases/download/v0.9.0/consul-template_0.9.0_linux_amd64.tar.gz
/tmp/consul-template.tar.gz  
RUN tar -xf /tmp/consul-template.tar.gz \  
&& mv consul-template_0.9.0_linux_amd64/consul-template /bin/consul-template \  
&& chmod a+x /bin/consul-template  
  
COPY ./files/start_lb.sh /usr/local/sbin/start_lb.sh  
COPY ./files/pre_init.py /usr/local/sbin/pre_init.py  
COPY ./files/hp_reinit.sh /usr/local/sbin/hp_reinit.sh  
COPY ./files/haproxy.ctmpl /etc/haproxy/haproxy.ctmpl  
COPY ./files/haproxy.cfg /etc/haproxy/haproxy.cfg  
  
RUN chmod u+x /usr/local/sbin/start_lb.sh \  
/usr/local/sbin/pre_init.py \  
/usr/local/sbin/hp_reinit.sh  
  
EXPOSE 1883 15672 3000 5601  
ENTRYPOINT [ "python", "/usr/local/sbin/pre_init.py" ]

