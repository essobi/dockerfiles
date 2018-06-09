FROM ubuntu:latest  
  
MAINTAINER Ailbirt Javier  
  
# Set this environment variable to true to set timezone on container start.  
ENV SET_CONTAINER_TIMEZONE False  
# Default container timezone as found under the directory
/usr/share/zoneinfo/.  
ENV CONTAINER_TIMEZONE America/Bogota  
# URL from which to download Elastalert.  
ENV ELASTALERT_URL https://github.com/Yelp/elastalert/archive/master.zip  
# Directory holding configuration for Elastalert and Supervisor.  
ENV CONFIG_DIR /opt/config  
# Elastalert rules directory.  
ENV RULES_DIRECTORY /opt/rules  
# Elastalert configuration file path in configuration directory.  
ENV ELASTALERT_CONFIG ${CONFIG_DIR}/elastalert_config.yaml  
# Directory to which Elastalert and Supervisor logs are written.  
ENV LOG_DIR /opt/logs  
# Elastalert home directory name.  
ENV ELASTALERT_DIRECTORY_NAME elastalert  
# Elastalert home directory full path.  
ENV ELASTALERT_HOME /opt/elastalert  
# Supervisor configuration file for Elastalert.  
ENV ELASTALERT_SUPERVISOR_CONF ${CONFIG_DIR}/elastalert_supervisord.conf  
# Alias, DNS or IP of Elasticsearch host to be queried by Elastalert. Set in
default Elasticsearch configuration file.  
ENV ELASTICSEARCH_HOST elasticsearchhost  
# Port on above Elasticsearch host. Set in default Elasticsearch configuration
file.  
ENV ELASTICSEARCH_PORT 9200  
# Use TLS to connect to Elasticsearch (True or False)  
ENV ELASTICSEARCH_TLS False  
# Verify TLS  
ENV ELASTICSEARCH_TLS_VERIFY False  
# ElastAlert writeback index  
ENV ELASTALERT_INDEX elastalert_status  
  
WORKDIR /opt  
  
# Copy the script used to launch the Elastalert when a container is started.  
COPY ./start-elastalert.sh /opt/  
  
# Install software required for Elastalert and NTP for time synchronization.  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get -y install build-essential python-setuptools python2.7
python2.7-dev libssl-dev git tox wget unzip  
RUN apt-get -y install ca-certificates openssl libffi-dev python-dev gcc musl-
dev tzdata openntpd  
  
# Install pip - required for installation of Elastalert.  
RUN easy_install pip  
  
# Download and unpack Elastalert.  
RUN wget -O elastalert.zip "${ELASTALERT_URL}" && \  
unzip elastalert.zip && \  
rm elastalert.zip && \  
mv e* "${ELASTALERT_HOME}"  
  
WORKDIR "${ELASTALERT_HOME}"  
  
RUN pip install -e .  
#RUN pip install -r requirements.txt  
#Downgrade dateutil to 2.6.1 version due to
https://github.com/Yelp/elastalert/issues/1602 bug.  
RUN pip uninstall -y "python-dateutil"  
RUN pip install "python-dateutil==2.6.1" \--force-reinstall  
  
# Install Elastalert.  
RUN python setup.py install  
  
# Install Supervisor.  
RUN easy_install supervisor  
  
# Make the start-script executable.  
RUN chmod +x /opt/start-elastalert.sh  
  
# Create directories. The /var/empty directory is used by openntpd.  
RUN mkdir -p ${CONFIG_DIR} && \  
mkdir -p ${RULES_DIRECTORY} && \  
mkdir -p ${LOG_DIR} && \  
mkdir -p /var/empty  
  
# Copy default configuration files to configuration directory.  
RUN cp ${ELASTALERT_HOME}/config.yaml.example ${ELASTALERT_CONFIG} && \  
cp ${ELASTALERT_HOME}/supervisord.conf.example ${ELASTALERT_SUPERVISOR_CONF}
&& \  
  
# Elastalert configuration:  
# Set the rule directory in the Elastalert config file to external rules
directory.  
sed -i -e"s|rules_folder: [[:print:]]*|rules_folder: ${RULES_DIRECTORY}|g"
${ELASTALERT_CONFIG} && \  
# Set the Elasticsearch host that Elastalert is to query.  
sed -i -e"s|es_host: [[:print:]]*|es_host: ${ELASTICSEARCH_HOST}|g"
${ELASTALERT_CONFIG} && \  
# Set the port used by Elasticsearch at the above address.  
sed -i -e"s|es_port: [0-9]*|es_port: ${ELASTICSEARCH_PORT}|g"
${ELASTALERT_CONFIG} && \  
  
# Elastalert Supervisor configuration:  
# Redirect Supervisor log output to a file in the designated logs directory.  
sed -i -e"s|logfile=.*log|logfile=${LOG_DIR}/elastalert_supervisord.log|g"
${ELASTALERT_SUPERVISOR_CONF} && \  
# Redirect Supervisor stderr output to a file in the designated logs
directory.  
sed -i
-e"s|stderr_logfile=.*log|stderr_logfile=${LOG_DIR}/elastalert_stderr.log|g"
${ELASTALERT_SUPERVISOR_CONF} && \  
# Modify the start-command.  
sed -i -e"s|python elastalert.py|python -m elastalert.elastalert --config
${ELASTALERT_CONFIG}|g" ${ELASTALERT_SUPERVISOR_CONF} && \  
  
# Copy the Elastalert configuration file to Elastalert home directory to be
used when creating index first time an Elastalert container is launched.  
cp ${ELASTALERT_CONFIG} ${ELASTALERT_HOME}/config.yaml  
  
# Clean up.  
RUN apt-get clean  
  
# Add Elastalert to Supervisord.  
RUN supervisord -c ${ELASTALERT_SUPERVISOR_CONF}  
  
# Define mount points.  
VOLUME [ "${CONFIG_DIR}", "${RULES_DIRECTORY}", "${LOG_DIR}"]  
  
# Launch Elastalert when a container is started.  
CMD ["/opt/start-elastalert.sh"]  

