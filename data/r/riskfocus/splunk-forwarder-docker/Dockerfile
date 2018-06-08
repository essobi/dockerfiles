# Tomcat 7 and JRE 7 are required for Validator  
# see https://registry.hub.docker.com/_/tomcat/ for full list of tomcat image
flavors  
FROM tomcat:8.0.23-jre8  
  
# Splunk Forwarder Default Directory  
ENV SPLUNK_HOME /opt/splunkforwarder  
  
# New versions and build numbers can be found at
http://www.splunk.com/download/universal-forwarder.html  
ENV SPLUNK_FORWARDER_VERSION 6.2.3  
ENV SPLUNK_FORWARDER_BUILD 264376  
ENV SPLUNK_FORWARDER_DEB_URL
https://download.splunk.com/products/splunk/releases/${SPLUNK_FORWARDER_VERSION}/universalforwarder/linux/splunkforwarder-${SPLUNK_FORWARDER_VERSION}-${SPLUNK_FORWARDER_BUILD}-linux-2.6-amd64.deb  
  
# Temporary environment variables - The following will have to be replaced by
arguments when calling docker -e flag  
#ENV SPLUNK_BASE_DATA_DIRECTORY /data/test  
#ENV SPLUNK_FORWARDER_INPUT_PARAMETERS "/rf-
validator.dat|validator|Validator:/rf-emulator.dat|validator|GTR Emulator"  
# We have to use --insecure since download.splunk.com provides stock
Cloudfront certificate with no custom domain  
RUN curl --insecure --show-error ${SPLUNK_FORWARDER_DEB_URL} -o
splunkforwarder.deb \  
&& dpkg -i splunkforwarder.deb \  
&& rm splunkforwarder.deb  
  
# Add Forwarder Inputs & Forwarder Outputs Config Apps  
ENV RISKFOCUS_FORWARDER_INPUTS_APP riskfocus_all_forwarder_inputs  
ENV RISKFOCUS_FORWARDER_OUTPUTS_APP riskfocus_all_forwarder_outputs  
COPY ${RISKFOCUS_FORWARDER_INPUTS_APP}
${SPLUNK_HOME}/etc/apps/${RISKFOCUS_FORWARDER_INPUTS_APP}  
COPY ${RISKFOCUS_FORWARDER_OUTPUTS_APP}
${SPLUNK_HOME}/etc/apps/${RISKFOCUS_FORWARDER_OUTPUTS_APP}  
  
# Normalization of ownership and mode to Splunk installation style  
RUN chown -R splunk:splunk
${SPLUNK_HOME}/etc/apps/${RISKFOCUS_FORWARDER_INPUTS_APP} \  
&& find ${SPLUNK_HOME}/etc/apps/${RISKFOCUS_FORWARDER_INPUTS_APP} -type f
-print0 | xargs -0 chmod 444 \  
&& find ${SPLUNK_HOME}/etc/apps/${RISKFOCUS_FORWARDER_INPUTS_APP} -type d
-print0 | xargs -0 chmod 755  
RUN chown -R splunk:splunk
${SPLUNK_HOME}/etc/apps/${RISKFOCUS_FORWARDER_OUTPUTS_APP} \  
&& find ${SPLUNK_HOME}/etc/apps/${RISKFOCUS_FORWARDER_OUTPUTS_APP} -type f
-print0 | xargs -0 chmod 444 \  
&& find ${SPLUNK_HOME}/etc/apps/${RISKFOCUS_FORWARDER_OUTPUTS_APP} -type d
-print0 | xargs -0 chmod 755  
  
# Applies Splunk Forwarder Configurations  
ENV RISKFOCUS_CONF_SCRIPT riskfocus_forwarder_configuration.sh  
ENV RISKFOCUS_CONF_SCRIPT_PATH ${SPLUNK_HOME}/bin/${RISKFOCUS_CONF_SCRIPT}  
COPY ${RISKFOCUS_CONF_SCRIPT} ${SPLUNK_HOME}/bin/  
RUN chown -R splunk:splunk ${RISKFOCUS_CONF_SCRIPT_PATH} && chmod 555
${RISKFOCUS_CONF_SCRIPT_PATH}  
  
CMD ${RISKFOCUS_CONF_SCRIPT_PATH} && /opt/splunkforwarder/bin/splunk start
--nodaemon --accept-license

