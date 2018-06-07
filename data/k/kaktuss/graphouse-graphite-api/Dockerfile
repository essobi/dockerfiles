FROM e11it/graphouse:latest  
  
ENV \  
CONSUL_TEMPLATE_VERSION=0.19.4 \  
CONSUL_TEMPLATE_SHA256=5f70a7fb626ea8c332487c491924e0a2d594637de709e5b430ecffc83088abc0
\  
  
CONSUL_HTTP_ADDR= \  
CONSUL_TOKEN=  
  
USER root  
  
RUN \  
apt-get update \  
  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
curl \  
unzip \  
  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
build-essential \  
libcairo2-dev \  
libffi-dev \  
python3-dev \  
python3-pip \  
  
&& cd /usr/local/bin \  
&& curl -L https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip -o consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& echo -n "$CONSUL_TEMPLATE_SHA256 consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" | sha256sum -c - \  
&& unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& rm consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
  
&& pip3 install \  
graphite-api \  
gunicorn \  
  
&& ln -fs /opt/graphouse/bin/graphouse_api.py /usr/local/lib/python3.4/dist-
packages/graphite_api/finders/graphouse_api.py \  
  
&& apt-get purge -y --auto-remove \  
curl \  
unzip \  
  
&& rm -rf /var/lib/apt/lists/*  
  
COPY templates /root/templates  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
  
EXPOSE 8000  
  
CMD ["/usr/local/bin/entrypoint.sh"]  

