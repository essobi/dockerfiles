FROM ubuntu:14.04  
MAINTAINER Kyoungmo yang <mo@embian.com>  
  
# Define Evn  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
##############################################  
# 1. Install required package  
##############################################  
# Install curl  
RUN apt-get install -y curl ruby  
  
##############################################  
# 2. Install Fluentd  
##############################################  
RUN curl -L http://toolbelt.treasuredata.com/sh/install-ubuntu-trusty-td-
agent2.sh | sh  
RUN td-agent-gem install fluent-plugin-record-reformer && \  
td-agent-gem install fluent-plugin-amqp2  
  
COPY plugin/in_tail_with_org_msg.rb /etc/td-agent/plugin/  
COPY conf/td-agent.conf /etc/td-agent/  
COPY script/access.rb /data/  
COPY script/error.rb /data/  
COPY script/run_test.sh /data/  
  
VOLUME ["/data"]  
  
RUN echo 'sed -i \' > /etc/td-agent/arms_init.sh && \  
echo '-e "s/DEFAULT_USER/`echo $DEFAULT_USER`/gi" \' >> /etc/td-
agent/arms_init.sh && \  
echo '-e "s/DEFAULT_PASS/`echo $DEFAULT_PASS`/gi" \' >> /etc/td-
agent/arms_init.sh && \  
echo '-e "s/HOST_NAME/`echo $HOST_NAME`/gi" \' >> /etc/td-agent/arms_init.sh
&& \  
echo '/etc/td-agent/td-agent.conf' >> /etc/td-agent/arms_init.sh && \  
chmod 755 /etc/td-agent/arms_init.sh  
  
RUN echo "/etc/td-agent/arms_init.sh" > /usr/bin/start.sh && \  
echo "service td-agent restart" >> /usr/bin/start.sh && \  
echo "sh /data/run_test.sh" >> /usr/bin/start.sh && \  
chmod 755 /usr/bin/start.sh  
  
CMD ["sh", "-c", "/usr/bin/start.sh"]  

