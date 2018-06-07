FROM alpine:3.4  
  
RUN apk add \--no-cache python py-pip py-setuptools git ca-certificates \  
&& pip install --no-cache-dir python-dateutil python-magic \  
&& git clone --depth=1 https://github.com/s3tools/s3cmd.git /opt/s3cmd \  
&& rm -rf /opt/s3cmd/.git \  
&& ln -s /opt/s3cmd/s3cmd /usr/bin/s3cmd \  
&& apk del py-pip py-setuptools git  
  
ADD ./files/.s3cfg /root/.s3cfg  
ADD ./files/main.sh /opt/main.sh  
  
# Main entrypoint script and directories for s3cmd  
RUN chmod u+x /opt/main.sh \  
&& mkdir /opt/src /opt/dest  
  
ENTRYPOINT ["/opt/main.sh"]  
CMD [""]  

