FROM ubuntu:trusty  
MAINTAINER Michael Shang <michael.shang@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -q update && \  
apt-get -y -q dist-upgrade && \  
apt-get -y -q install rsyslog python-setuptools python-pip curl  
  
RUN curl https://s3.amazonaws.com/aws-cloudwatch/downloads/latest/awslogs-
agent-setup.py -o awslogs-agent-setup.py  
  
RUN sed -i "s/#\$ModLoad imudp/\$ModLoad imudp/" /etc/rsyslog.conf && \  
sed -i "s/#\$UDPServerRun 514/\$UDPServerRun 514/" /etc/rsyslog.conf && \  
sed -i "s/#\$ModLoad imtcp/\$ModLoad imtcp/" /etc/rsyslog.conf && \  
sed -i "s/#\$InputTCPServerRun 514/\$InputTCPServerRun 514/" /etc/rsyslog.conf  
  
COPY awslogs.conf awslogs.conf  
RUN python ./awslogs-agent-setup.py -n -r ap-southeast-2 -c /awslogs.conf  
  
RUN pip install supervisor  
COPY supervisord.conf /usr/local/etc/supervisord.conf  
  
EXPOSE 514/tcp 514/udp  
CMD ["/usr/local/bin/supervisord"]  

