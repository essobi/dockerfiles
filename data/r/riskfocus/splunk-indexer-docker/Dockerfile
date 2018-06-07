FROM buildpack-deps:jessie-curl  
  
# new versions and build numbers can be found at
https://www.splunk.com/download/splunk-enterprise.html  
ENV SPLUNK_VERSION 6.2.2  
ENV SPLUNK_BUILD 255606  
ENV SPLUNK_DEB_URL
https://download.splunk.com/products/splunk/releases/${SPLUNK_VERSION}/splunk/linux/splunk-${SPLUNK_VERSION}-${SPLUNK_BUILD}-linux-2.6-amd64.deb  
  
# we have to use --insecure since download.splunk.com provides stock
Cloudfront certificate with no custom domain  
RUN curl --insecure --show-error ${SPLUNK_DEB_URL} -o splunk.deb \  
&& dpkg -i splunk.deb \  
&& rm splunk.deb  
  
# enable listening on localhost:9997 for forwarder connections  
ENV splunkInputCfg /opt/splunk/etc/system/local/inputs.conf  
COPY inputs.conf ${splunkInputCfg}  
  
# normalization of ownership and mode to splunk installation style  
RUN chown splunk:splunk ${splunkInputCfg} \  
&& chmod 444 ${splunkInputCfg}  
  
EXPOSE 9997  
EXPOSE 8000  
CMD /opt/splunk/bin/splunk start --accept-license --nodaemon  

