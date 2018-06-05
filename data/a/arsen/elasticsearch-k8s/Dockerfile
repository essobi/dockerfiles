FROM elasticsearch:1.6  
RUN /usr/share/elasticsearch/bin/plugin -install io.fabric8/elasticsearch-
cloud-kubernetes/1.3.0  
RUN /usr/share/elasticsearch/bin/plugin -install mobz/elasticsearch-head  
  
RUN mkdir /data  
  
# Trust Kubernetes Certificate, used for kubernetes elasticsearch discovery  
ENV KUBERNETES_TRUST_CERT true  
  
ENV CLUSTER_NAME default_cluster_name  
ENV SERVICE_DNS default_service_dns  
ENV NODE_DATA true  
ENV HTTP_ENABLED true  
  
COPY config/ /usr/share/elasticsearch/config/  

