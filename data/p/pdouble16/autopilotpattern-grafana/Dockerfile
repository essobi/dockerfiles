FROM pdouble16/autopilotpattern-base:1.2.0  
FROM grafana/grafana:4.3.2  
RUN mkdir -p /var/lib/consul /etc/consul  
COPY \--from=0 /usr/local/bin/* /usr/local/bin/  
COPY \--from=0 /etc/consul/* /etc/consul/  
  
ENV CONTAINERPILOT="/etc/containerpilot.json5"  
RUN rm -rf /var/lib/apt/lists/* && apt-get -q update &&\  
apt-get install -qy --force-yes --no-install-recommends \  
curl unzip python3 python3-pip jq &&\  
apt-get clean &&\  
pip3 install grafanalib &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -rf /tmp/* \  
# Install Consul template, releases at https://releases.hashicorp.com/consul-
template/  
&& export CONSUL_TEMPLATE_VERSION=0.18.5 \  
&& export
CONSUL_TEMPLATE_CHECKSUM=b0cd6e821d6150c9a0166681072c12e906ed549ef4588f73ed58c9d834295cd2
\  
&& curl --retry 7 \--fail -Lso /tmp/consul-template.zip
"https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" \  
&& echo "${CONSUL_TEMPLATE_CHECKSUM} /tmp/consul-template.zip" | sha256sum -c
\  
&& unzip /tmp/consul-template.zip -d /usr/local/bin \  
&& rm /tmp/consul-template.zip  
  
RUN mkdir -p /grafana/dashboards &&\  
curl --fail -so /grafana/dashboards/nginx.json
https://grafana.com/api/dashboards/462/revisions/1/download &&\  
curl --fail -so /grafana/dashboards/docker.json
https://grafana.com/api/dashboards/893/revisions/5/download  
  
RUN curl --fail -sL https://github.com/percona/grafana-
dashboards/archive/v1.1.4.tar.gz |\  
tar -xz -f - -C /tmp &&\  
cp /tmp/grafana-dashboards-1.1.4/dashboards/Disk_* /grafana/dashboards/ &&\  
cp /tmp/grafana-dashboards-1.1.4/dashboards/MongoDB_* /grafana/dashboards/ &&\  
cp /tmp/grafana-dashboards-1.1.4/dashboards/Prometheus.json
/grafana/dashboards/ &&\  
cp /tmp/grafana-dashboards-1.1.4/dashboards/Summary_Dashboard.json
/grafana/dashboards/ &&\  
cp /tmp/grafana-dashboards-1.1.4/dashboards/System_Overview.json
/grafana/dashboards/ &&\  
cp /tmp/grafana-dashboards-1.1.4/dashboards/Trends_Dashboard.json
/grafana/dashboards/ &&\  
rm -rf /tmp/grafana-dashboards-1.1.4  
  
RUN for F in $(ls dashboards/*.dashboard.py 2>/dev/null); do generate-
dashboard -o /grafana/dashboards/${F/.dashboard.py/.json} ${F}; done  
COPY dashboards/*.json /grafana/dashboards/  
  
RUN sed -r -i -e 's/[$][{]DS_.*?[}]/Prometheus/g' -e
's/job="prometheus"/job="containerpilot"/g' -e
's/label_values(cluster)/label_values(set)/g' /grafana/dashboards/*.json &&\  
sed -r -i \  
-e 's/label_values\\(cluster\\)/label_values\\(set\\)/g' \  
-e 's/cluster=/set=/g' \  
-e 's/mongodb_mongod_connections\\{set=[^}]*\\}/mongodb_mongod_connections\\{\\}/g' \  
-e 's/mongodb_mongod_storage_engine\\{set=[^,}]*,/mongodb_mongod_storage_engine\\{/g' \  
/grafana/dashboards/MongoDB_*.json &&\  
sed -r -i 's/job=\\\"kafka\\\"/job=\\\"containerpilot\\\"/g'
/grafana/dashboards/kafka.json  
  
COPY bin/* /usr/local/bin/  
COPY etc/grafana.ini /etc/grafana/grafana.ini  
COPY etc/containerpilot.json5 ${CONTAINERPILOT}  
  
ONBUILD RUN for F in $(ls dashboards/*.dashboard.py 2>/dev/null); do generate-
dashboard -o /grafana/dashboards/${F/.dashboard.py/.json} ${F}; done  
ONBUILD RUN cp dashboards/*.json /grafana/dashboards/ || exit 0  
  
ENTRYPOINT [ "/usr/local/bin/containerpilot" ]  
  
HEALTHCHECK \--interval=60s --timeout=10s --retries=3 CMD /usr/bin/test "$(cat
/var/run/healthcheck)" = "0" || exit 1  
  
LABEL maintainer='Patrick Double "pat@patdouble.com"' \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.license="Apache-2.0" \  
org.label-schema.name="Autopilot Pattern for Grafana + Prometheus Monitoring"
\  
org.label-schema.url="https://bitbucket.org/double16/autopilotpattern-grafana"
\  
org.label-schema.docker.dockerfile="${DOCKERFILE_PATH}/Dockerfile" \  
org.label-schema.vcs-ref=$SOURCE_REF \  
org.label-schema.vcs-type='git' \  
org.label-schema.vcs-url="https://bitbucket.org/double16/autopilotpattern-
grafana.git"  

