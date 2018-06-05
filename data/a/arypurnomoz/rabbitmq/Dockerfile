# using debian will break it  
FROM ubuntu:trusty  
  
ADD http://www.rabbitmq.com/rabbitmq-signing-key-public.asc /tmp/rabbit.asc  
  
ADD run.sh /tmp/run.sh  
  
RUN \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F7B8CEA6056E8E56 \  
&& echo "deb http://www.rabbitmq.com/debian/ testing main" >
/etc/apt/sources.list.d/rabbitmq.list \  
&& apt-get update \  
&& apt-get upgrade -y \  
&& apt-get -y install rabbitmq-server \  
&& rabbitmq-plugins enable rabbitmq_management \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD rabbitmq.config /etc/rabbitmq/rabbitmq.config  
  
EXPOSE 5671 15672  
ENTRYPOINT ["/tmp/run.sh"]  

