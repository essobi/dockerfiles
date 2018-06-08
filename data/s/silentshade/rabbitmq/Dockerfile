FROM rabbitmq:alpine  
  
RUN set -ex; \  
\  
apk add --no-cache --virtual .build-deps \  
ca-certificates \  
gnupg \  
libressl \  
tar \  
xz \  
; \  
\  
wget -O "$RABBITMQ_HOME/plugins/rabbitmq_delayed_message_exchange-0.0.1.ez"
"https://bintray.com/rabbitmq/community-
plugins/download_file?file_path=rabbitmq_delayed_message_exchange-0.0.1.ez"; \  
apk del .build-deps  
  
RUN rabbitmq-plugins enable --offline rabbitmq_delayed_message_exchange  

