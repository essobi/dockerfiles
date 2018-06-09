FROM ubuntu:latest  
MAINTENER Ryuta Otaki <otaki.ryuta@classmethod.jp>  
  
RUN apt-get update  
RUN apt-get install -q -y python python-pip wget  
RUN wget https://s3.amazonaws.com/aws-cloudwatch/downloads/awslogs-agent-
setup-v1.0.py  
RUN chmod +x ./awslogs-agent-setup-v1.0.py  
ADD awslogs.conf.dummy ./awslogs.conf  
RUN ./awslogs-agent-setup-v1.0.py -n -r us-east-1 -c ./awslogs.conf  
ONBUILD ADD aws.conf /var/awslogs/etc/aws.conf  
ONBUILD ADD awslogs.conf /var/awslogs/etc/awslogs.conf  
CMD /bin/sh /var/awslogs/bin/awslogs-agent-launcher.sh  
  

