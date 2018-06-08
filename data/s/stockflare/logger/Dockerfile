FROM ubuntu:trusty  
MAINTAINER David Kelley <david@stockflare.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV CONFD_VERSION 0.10.0  
ENV AWS_REGION us-east-1  
ENV CLOUDWATCH_LOG_GROUP default  
  
RUN apt-get -q update && \  
apt-get -y -q dist-upgrade && \  
apt-get -y -q install rsyslog python-setuptools python-pip curl wget  
  
RUN sed -i "s/#\$ModLoad imudp/\$ModLoad imudp/" /etc/rsyslog.conf && \  
sed -i "s/#\$UDPServerRun 514/\$UDPServerRun 514/" /etc/rsyslog.conf && \  
sed -i "s/#\$ModLoad imtcp/\$ModLoad imtcp/" /etc/rsyslog.conf && \  
sed -i "s/#\$InputTCPServerRun 514/\$InputTCPServerRun 514/" /etc/rsyslog.conf  
  
RUN sed -i "s/authpriv.none/authpriv.none,local6.none,local7.none/"
/etc/rsyslog.d/50-default.conf  
  
RUN echo "if \$syslogfacility-text == 'local6' then /var/log/cloudwatch.log"
>> /etc/rsyslog.d/http.conf && \  
echo "if \$syslogfacility-text == 'local6' then ~" >> /etc/rsyslog.d/http.conf  
  
RUN wget --progress=bar:force --retry-connrefused -t 5
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 -O /bin/confd && \  
chmod +x /bin/confd  
  
ADD etc/confd /etc/confd  
  
RUN pip install supervisor  
  
WORKDIR /aws  
  
RUN curl https://s3.amazonaws.com/aws-cloudwatch/downloads/latest/awslogs-
agent-setup.py -o awslogs-agent-setup.py  
  
ADD boot boot  
  
EXPOSE 514/tcp 514/udp  
  
CMD ["./boot"]  

