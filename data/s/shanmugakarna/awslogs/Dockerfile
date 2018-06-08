FROM ubuntu:15.10  
MAINTAINER DSB Ops <dsbawsops@dsbconsulting.net>  
RUN apt-get update && apt-get install -q -y python python-pip wget supervisor  
RUN wget https://s3.amazonaws.com/aws-cloudwatch/downloads/latest/awslogs-
agent-setup.py  
RUN chmod +x ./awslogs-agent-setup.py  
ADD awslogs.conf ./awslogs.conf  
RUN mkdir -p /etc/cron.d/  
RUN ./awslogs-agent-setup.py -n -r us-east-1 -c ./awslogs.conf  
ADD ./awslogs /usr/bin/awslogs  
ADD ./awslog-supervisor.conf /etc/supervisor/conf.d/awslogs.conf  
  
ONBUILD ADD awslogs.conf /var/awslogs/etc/awslogs.conf  
  
CMD ["supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]  

