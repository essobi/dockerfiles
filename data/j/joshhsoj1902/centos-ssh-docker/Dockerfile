FROM jdeathe/centos-
ssh:latest@sha256:da6069a83e1ab84b7e471827f416fe4053337417dd03e7cdf35c4ca8fca807ef  
  
RUN yum install -y wget \  
&& wget -qO- https://get.docker.com/ | sh \  
&& systemctl enable docker.service  
  
RUN yum install -y python-pip \  
&& pip install docker-compose

