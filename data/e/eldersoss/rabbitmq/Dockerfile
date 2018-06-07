FROM rabbitmq:3.7.2-management  
  
MAINTAINER Elders  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends wget \  
&& apt-get install -y p7zip-full  
  
RUN wget --no-check-certificate https://dl.bintray.com/rabbitmq/community-
plugins/3.7.0/rabbitmq_delayed_message_exchange-3.7.0.zip -P
usr/lib/rabbitmq/lib/rabbitmq_server-3.7.2/plugins/  
  
RUN 7z e
usr/lib/rabbitmq/lib/rabbitmq_server-3.7.2/plugins/rabbitmq_delayed_message_exchange-3.7.0.zip
-o/usr/lib/rabbitmq/lib/rabbitmq_server-3.7.2/plugins/  
  
RUN rabbitmq-plugins enable rabbitmq_delayed_message_exchange  

