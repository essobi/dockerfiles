FROM rabbitmq  
  
# RUN apt-get update && \  
# apt-get install -y curl libcurl3 lsb-release  
  
# RUN curl -o /etc/apt/sources.list.d/stackdriver.list
https://repo.stackdriver.com/jessie.list  
# RUN curl --silent https://app.stackdriver.com/RPM-GPG-KEY-stackdriver |apt-
key add -  
# RUN apt-get update && \  
# apt-get install -y stackdriver-agent  
  
# RUN curl -O https://repo.stackdriver.com/stack-install.sh && \  
# bash stack-install.sh \--write-gcm  
  
# COPY rabbitmq.conf /opt/stackdriver/collectd/etc/collectd.d/rabbitmq.conf  
# RUN service stackdriver-agent restart  
  
RUN rabbitmq-plugins enable --offline rabbitmq_management rabbitmq_web_stomp  
  
EXPOSE 15671 15672 15674  

