FROM rabbitmq  
  
MAINTAINER Liang Shi <jeremy@pda.sh>  
  
# install python  
RUN apt update && apt install -y python3.4 wget  
  
# download rabbitmqadmin script  
RUN wget https://raw.githubusercontent.com/rabbitmq/rabbitmq-
management/rabbitmq_v3_6_12/bin/rabbitmqadmin -P /tmp && \  
mv /tmp/rabbitmqadmin /usr/local/bin && \  
chmod a+x /usr/local/bin/rabbitmqadmin && \  
ln -s /usr/bin/python3.4 /usr/bin/python  
  
# enable rabbitmq plugin  
RUN rabbitmq-plugins enable \--offline rabbitmq_management  
  
# clean up  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 15671 15672  

