FROM rabbitmq:3.6.6-management  
  
ENV RABBITMQ_CLUSTERER_VERSION 1.0.3  
  
ENV RABBITMQ_BOOT_MODULE rabbit_clusterer  
  
ENV RABBITMQ_SERVER_ADDITIONAL_ERL_ARGS "-pa
/plugins/rabbitmq_clusterer.ez/rabbitmq_clusterer-${RABBITMQ_CLUSTERER_VERSION}/ebin"  
  
RUN apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& wget -O /plugins/rabbitmq_clusterer.ez
"https://bintray.com/rabbitmq/community-
plugins/download_file?file_path=rabbitmq_clusterer-${RABBITMQ_CLUSTERER_VERSION}.ez"
\  
&& rabbitmq-plugins enable rabbitmq_clusterer --offline \  
&& apt-get purge -y --auto-remove ca-certificates wget  

