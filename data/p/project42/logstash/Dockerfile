#Install and configure []  
  
FROM project42/s6-centos:centos7  
MAINTAINER Brandon Cone - bcone@esu10.org  
  
COPY container_files /  
  
# I'm not certain we actually need to run anything since we're extending the
existing logstash image...Pending test.  
# WORKDIR /tmp/logstash  
# ENTRYPOINT ["/bin/bash"]  
# RUN logstash-plugin install logstash-output-mqtt  
RUN yum install -y git  
# && \  
# export LOGSTASH_DIR=/tmp/logstash/logstash-config  
  
# CMD ["/scripts/run.sh", "/tmp", "logstash-config",
"git@git.ops.esu10.org:Operations/logstash-config.git"]  
# CMD ["logstash-config", "git@git.ops.esu10.org:Operations/logstash-
config.git"]

