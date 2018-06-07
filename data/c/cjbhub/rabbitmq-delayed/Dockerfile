FROM rabbitmq:3.6.10-management  
  
LABEL maintainer="cjbarre@gmail.com" \  
version="1.0"  
  
ENV url https://bintray.com/rabbitmq/community-
plugins/download_file?file_path=rabbitmq_delayed_message_exchange-0.0.1.ez  
  
RUN apt-get update && apt-get install -y wget ca-certificates  
  
RUN wget -O /plugins/delayed_exchange.ez $url \  
&& cd /plugins \  
&& rabbitmq-plugins enable \--offline rabbitmq_delayed_message_exchange  

