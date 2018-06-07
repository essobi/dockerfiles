FROM bbania/centos:base  
MAINTAINER "Bart Bania" <contact@bartbania.com>  
  
RUN yum install -y haproxy socat iptables  
RUN yum install -y supervisor  
RUN yum install -y python-pip python-devel gcc && \  
pip install --upgrade pip && \  
pip install mycli  
RUN yum erase -y python-devel && \  
yum clean all  
  
RUN ln -s /usr/bin/mycli /usr/bin/mysql  
RUN mkdir -p /etc/haproxy/{supervisor,scripts}  
  
COPY ./etc/supervisord.service /usr/lib/systemd/system/supervisord.service  
COPY ./etc/haproxy.cfg /etc/haproxy/haproxy.cfg  
COPY ./etc/supervisord.conf /etc/haproxy/supervisor/supervisord.conf  
COPY ./etc/supervisord.d/haproxy-alert.ini /etc/haproxy/supervisor/d/haproxy-
alert.ini  
COPY ./etc/alert.py /etc/haproxy/scripts/  
COPY ./etc/iptables /etc/sysconfig/iptables  
  
VOLUME "/etc/haproxy"  
  
EXPOSE 3306 80  

