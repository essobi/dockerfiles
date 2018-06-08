FROM solr:5  
LABEL maintainer "jamiejaxon@gmail.com"  
  
ENV server_root_path=/opt/solr/server  
ENV lib_path=${server_root_path}/lib  
  
# change to root user temporarily for the following RUNs  
USER root  
  
################################################################################  
# This is all part of an elaborate workaround to  
# https://issues.apache.org/jira/browse/SOLR-9725  
# Once that ticket's fixed, we won't need this part.  
# TODO: Once we've got this Dockerfile dialed in, remove unnecessary packages,  
# like inotify-tools, vim  
RUN mkdir -p ${server_root_path}/workaround && \  
touch ${server_root_path}/workaround/hashpwd.txt && \  
chown solr:solr -R ${server_root_path}/workaround && \  
apt-get update && apt-get install -y inotify-tools python vim && \  
curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py |
python && \  
pip install pywatch && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY workaround/generate_data_config_file.sh \  
workaround/sleep_until_modified.sh \  
${server_root_path}/workaround/  
COPY workaround/workaround_controller.sh /docker-entrypoint-initdb.d/  
  
RUN chown solr:solr -R ${server_root_path}/workaround && \  
mkdir "/opt/solr/data" && \  
chown -R solr:solr "/opt/solr/data"  
  
#==============================================================================#  
# change the container user back to Solr for future use  
USER ${SOLR_USER}  

