FROM datadog/docker-dd-agent:latest  
  
RUN echo ' collect_labels_as_tags: ["empire.app.name", "empire.app.release",
"empire.app.id", "empire.app.process"]' >> /etc/dd-
agent/conf.d/docker_daemon.yaml  

