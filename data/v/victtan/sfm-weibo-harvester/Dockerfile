FROM python:2.7  
MAINTAINER Vict Tan <ychtan@gwu.edu>  
  
RUN apt-get update && apt-get install -y \  
wget \  
zip  
#Upgrade pip  
RUN pip install --upgrade pip  
#Install the requirement  
ADD https://raw.githubusercontent.com/gwu-libraries/sfm-weibo-
harvester/master/requirements.txt /tmp/  
RUN pip install -r /tmp/requirements.txt  
RUN pip install appdeps  
#It should mounted as your development dir  
WORKDIR /opt/sfm-weibo-harvester  
  
# setting up the sfm-utils  
CMD cd /opt/sfm-utils \  
&& python setup.py develop \  
&& cd /opt/sfm-weibo-harvester \  
&& appdeps.py --port-wait mq:5672 \  
&& python weibo_harvester.py --debug=$DEBUG service mq
$MQ_ENV_RABBITMQ_DEFAULT_USER $MQ_ENV_RABBITMQ_DEFAULT_PASS  

