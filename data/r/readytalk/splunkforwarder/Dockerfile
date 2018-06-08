FROM debian:wheezy  
  
ENV REEFER_VERSION v0.0.4  
ENV SPLUNK_FORWARDER_VERSION 6.2.2  
ENV SPLUNK_FORWARDER_BUILD 255606  
ENV SPLUNK_FORWARDER_DEB_URL
https://download.splunk.com/products/splunk/releases/${SPLUNK_FORWARDER_VERSION}/universalforwarder/linux/splunkforwarder-${SPLUNK_FORWARDER_VERSION}-${SPLUNK_FORWARDER_BUILD}-linux-2.6-amd64.deb  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends curl procps ca-certificates && \  
curl -L https://github.com/docker-
infra/reefer/releases/download/${REEFER_VERSION}/reefer.gz | \  
gunzip >/usr/bin/reefer && \  
chmod a+x /usr/bin/reefer && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/apt/*  
  
RUN curl --show-error ${SPLUNK_FORWARDER_DEB_URL} -o splunkforwarder.deb \  
&& dpkg -i splunkforwarder.deb \  
&& rm splunkforwarder.deb  
  
COPY templates /templates  
  
ENTRYPOINT [ "/usr/bin/reefer", \  
"-t",
"/templates/inputs.conf:/opt/splunkforwarder/etc/apps/SplunkUniversalForwarder/local/inputs.conf",
\  
"-t",
"/templates/outputs.conf:/opt/splunkforwarder/etc/apps/SplunkUniversalForwarder/local/outputs.conf",
\  
"-E" \  
]  
  
CMD [ "/opt/splunkforwarder/bin/splunk", "start", "--accept-license", "--
nodaemon", "--no-prompt", "--answer-yes" ]  

