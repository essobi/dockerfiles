FROM deliveryagent/centos  
MAINTAINER Tommy McNeely <tommy@lark-it.com>  
  
# Install dependencies  
RUN yum -y install \  
cronie \  
curl \  
initscripts \  
python-pip \  
python-setuptools \  
rsyslog \  
supervisor \  
which \  
&& yum clean all  
  
# Install awslogs agent  
ENV REGION="us-west-2"  
COPY awslogs.conf awslogs.conf  
RUN curl -sSL https://s3.amazonaws.com/aws-
cloudwatch/downloads/latest/awslogs-agent-setup.py -o awslogs-agent-setup.py \  
&& python ./awslogs-agent-setup.py -n -r $REGION -c /awslogs.conf \  
&& yum clean all  
  
# Configure rsyslogd  
RUN sed -i -e "s/#\$ModLoad imudp/\$ModLoad imudp/" \  
-e "s/#\$UDPServerRun 514/\$UDPServerRun 514/" \  
-e "s/#\$ModLoad imtcp/\$ModLoad imtcp/" \  
-e "s/#\$InputTCPServerRun 514/\$InputTCPServerRun 514/" \  
-e "s/authpriv.none/authpriv.none;local6.none;local7.none/" /etc/rsyslog.conf  
COPY rsyslog.d /etc/rsyslog.d/  
  
# Configure LogRotate (TODO: start logrotate periodically)  
COPY logrotate.d /etc/logrotate.d/  
  
# Configure supervisord  
COPY supervisord.conf /etc/supervisord.conf  
  
EXPOSE 514/tcp 514/udp  
CMD ["/usr/local/bin/supervisord"]  

