FROM prom/alertmanager:v0.12.0  
  
ARG version="0.1.0-dev"  
ARG build_date="unknown"  
ARG commit_hash="unknown"  
ARG vcs_url="unknown"  
ARG vcs_branch="unknown"  
  
LABEL org.label-schema.vendor="Softonic" \  
org.label-schema.name="alertmanager" \  
org.label-schema.description="Prometheus Alertmanager with Slack and Logstash
receivers" \  
org.label-schema.usage="/src/README.md" \  
org.label-schema.url="https://github.com/bvis/docker-
alertmanager/blob/master/README.md" \  
org.label-schema.vcs-url=$vcs_url \  
org.label-schema.vcs-branch=$vcs_branch \  
org.label-schema.vcs-ref=$commit_hash \  
org.label-schema.version=$version \  
org.label-schema.schema-version="1.0" \  
org.label-schema.docker.cmd.devel="" \  
org.label-schema.docker.params="SLACK_API=Slack API endpoint,\  
LOGSTASH_URL=Logstash URL to send the alerts" \  
org.label-schema.build-date=$build_date  
  
ENV ALERTMANAGER_BIN="/bin/alertmanager" \  
SLACK_API="null" \  
LOGSTASH_URL="http://logstash:8080/"  
  
COPY rootfs /  
  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  
CMD [ "-config.file=/etc/alertmanager/config.yml", \  
"-storage.path=/alertmanager" ]  

