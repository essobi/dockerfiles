FROM logstash:5  
# Install logstash plugins.  
RUN logstash-plugin install logstash-input-journald logstash-output-
elasticsearch logstash-input-beats  
  
# Create a volume for storing state, set it as a default for the journald
plugin  
# to store the cursor.  
VOLUME /var/lib/logstash-journald  
ENV SINCEDB_DIR=/var/lib/logstash-journald  
  
# Override the entrypoint script from the base image to ensure Logstash runs  
# as root, which is required to access the journal.  
WORKDIR /  
COPY ./docker-entrypoint.sh ./  

