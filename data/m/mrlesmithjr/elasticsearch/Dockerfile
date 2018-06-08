FROM mrlesmithjr/alpine-ansible-java  
  
MAINTAINER Larry Smith Jr. <mrlesmithjr@gmail.com>  
  
# Copy Ansible Related Files  
COPY config/ansible/ /  
  
# Define Elasticsearch version to install  
ENV ELASTICSEARCH_MAJOR_VERSION="5.x" \  
ELASTICSEARCH_VER="5.2.2"  
# Run Ansible playbook  
RUN ansible-playbook -i "localhost," -c local /playbook.yml \  
\--extra-vars "elasticsearch_major_version=$ELASTICSEARCH_MAJOR_VERSION \  
elasticsearch_ver=$ELASTICSEARCH_VER" && \  
rm -rf /tmp/* && \  
rm -rf /var/cache/apk/*  
  
ENV PATH /usr/share/elasticsearch/bin:$PATH  
  
# Copy Docker Entrypoint  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
COPY config/elasticsearch /usr/share/elasticsearch/config  
  
# Setup volume  
VOLUME /usr/share/elasticsearch/data  
  
# Expose port(s)  
EXPOSE 9200 9300  
# Container start-up  
CMD ["elasticsearch"]  

