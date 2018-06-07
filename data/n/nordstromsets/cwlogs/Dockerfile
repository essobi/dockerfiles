FROM ubuntu  
  
MAINTAINER Tom Jackson thomas.jackson@nordstrom.com  
  
# Define env variables that will allow all containers to navigate the  
# Nordstrom outbound proxy .  
# You only need these if you are building on-prem.  
# Make sure to comment out before building on Docker Hub.  
# ENV http_proxy http://pbcld-proxy.nordstrom.net:3128  
# ENV https_proxy https://pbcld-proxy.nordstrom.net:3128  
# ENV no_proxy localhost,10.0.0/8,nordstrom.net  
# A required input is the configuration file defining the logs you want
aggregated. See exmaple  
# in congis/awslogs-example.conf for an example.  
# The conf file must be specified as an S3 URL, e.g.  
# s3://<bucket name>/<path to file>  
ENV CONFIGS_S3_URL TBD  
  
# cwlogs agent version  
# can see all available versions here:  
# http://aws-cloudwatch.s3-website-us-east-1.amazonaws.com/awscli-cwlogs/  
ENV AGENT_VER 1.3.1  
# Another input is the region your cloud watch logs group lives in  
ENV REGION us-west-2  
RUN apt-get update  
RUN apt-get -y install wget  
RUN apt-get -y install curl  
RUN apt-get -y install python  
  
# install awscli and boto, but of which are required by logs agent  
RUN apt-get install python-pip python-dev build-essential -y  
RUN pip install awscli  
RUN pip install boto  
  
# install plugin to add "aws logs push" argument to the "aws logs" command in
awscli  
RUN pip install --extra-index-url=http://aws-cloudwatch.s3-website-us-
east-1.amazonaws.com/ awscli-cwlogs==$AGENT_VER  
RUN aws configure set plugins.cwlogs cwlogs  
  
# create agent state dir, used as a DB by logs agent  
RUN mkdir -p /var/awslogs/state  
RUN chmod 777 /var/awslogs/state  
  
# Add boto config file to reduce risk of s3 read/write timeouts  
ADD configs/boto.cfg /etc/boto.cfg  
  
# Agent installation directory  
ENV AGENT_INSTALL /var/awslogs/bin  
  
# Add awslogs config file  
ADD configs/aws.conf $AGENT_INSTALL/aws.conf  
  
# Add the shell script that downloads the config file at container start time
then  
# launches the agent in the foreground  
ADD configs/cwlogs_startup.sh $AGENT_INSTALL/cwlogs_startup.sh  
RUN chmod 0777 $AGENT_INSTALL/cwlogs_startup.sh  
  
WORKDIR $AGENT_INSTALL  
  
# get agent setup script  
# RUN wget https://s3.amazonaws.com/aws-cloudwatch/downloads/latest/awslogs-
agent-setup.py  
# Fire up agent  
CMD ["./cwlogs_startup.sh"]  

