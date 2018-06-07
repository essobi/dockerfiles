FROM google/cloud-sdk:181.0.0-alpine  
  
ENV COMPOSE_VERSION 1.17.1  
ENV DOCKER_VERSION 17.12.0-ce  
ENV HELM_VERSION 2.8.1  
RUN apk add --no-cache curl make gettext bash py-pip openssl && \  
curl -fSL
"https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz"
-o docker.tgz \  
&& tar -xzvf docker.tgz \  
&& mv docker/* /usr/local/bin/ \  
&& rmdir docker \  
&& rm docker.tgz \  
&& docker -v \  
&& pip install "docker-compose==${COMPOSE_VERSION}" \  
&& gcloud components install kubectl --quiet \  
&& curl -fSL "https://storage.googleapis.com/kubernetes-
helm/helm-v${HELM_VERSION}-linux-amd64.tar.gz" -o helm.tgz \  
&& tar -xzvf helm.tgz \  
&& mv linux-amd64/helm /usr/local/bin/ \  
&& chmod +x /usr/local/bin/helm \  
&& rm helm.tgz \  
&& rm -rf linux-amd64 \  
&& helm version -c  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
ADD scripts /scripts  
RUN chmod -R +rwx scripts  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
CMD ["sh"]  

