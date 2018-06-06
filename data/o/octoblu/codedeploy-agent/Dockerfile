FROM ubuntu:14.04  
MAINTAINER Octoblu <docker@octoblu.com>  
# from
https://github.com/fortesinformatica/dockerfiles/tree/master/codedeploy-agent  
RUN mkdir -p /deploy  
VOLUME /deploy  
  
RUN apt-get update && \  
apt-get -qy install python-pip groff-base ruby2.0 gdebi curl && \  
pip install awscli && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /opt/codedeploy-agent  
  
WORKDIR /opt/codedeploy-agent  
  
RUN curl -O https://s3-us-west-2.amazonaws.com/aws-codedeploy-us-
west-2/latest/install  
  
RUN chmod +x install  
RUN ./install auto  
  
CMD service codedeploy-agent start-no-update && tail -qF -n 0
/var/log/aws/codedeploy-agent/codedeploy-agent.log  

