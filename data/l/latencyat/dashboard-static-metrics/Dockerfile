FROM latencyat/dashboard  
  
# Disable "All" view b/c it would blow up the browser  
RUN jq '.templating.list[0].includeAll=false' \  
/etc/grafana/dashboards/HTTP-Duration\ Site\ per\ Region.json > /tmp/x && \  
mv /tmp/x /etc/grafana/dashboards/HTTP-Duration\ Site\ per\ Region.json  
  
ENTRYPOINT [ "sh", "-c", \  
"curl -sfLo /etc/prometheus/prometheus.yml
https://pub.latency.at/prometheus.yml \  
&& exec /etc/entrypoint" ]  

