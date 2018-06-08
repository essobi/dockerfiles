FROM rabbitmq:latest  
  
ENV RABBITMQ_DELAYED_VERSION 0.0.1  
  
RUN buildDeps=" \  
ca-certificates \  
curl \  
" \  
&& set -x \  
&& DEBIAN_FRONTEND=noninteractive apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y $buildDeps --no-install-
recommends \  
&& curl -sSL \  
-o /usr/lib/rabbitmq/lib/rabbitmq_server-${RABBITMQ_VERSION}/plugins/rabbitmq_delayed_message_exchange-${RABBITMQ_DELAYED_VERSION}.ez \  
"https://bintray.com/rabbitmq/community-
plugins/download_file?file_path=rabbitmq_delayed_message_exchange-${RABBITMQ_DELAYED_VERSION}.ez"
\  
&& rabbitmq-plugins enable --offline rabbitmq_delayed_message_exchange \  
&& DEBIAN_FRONTEND=noninteractive apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false $buildDeps \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

