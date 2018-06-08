FROM fedora/python:latest  
  
USER root  
RUN curl -Lo /usr/local/bin/speedtest-cli
https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py && \  
chmod a+x /usr/local/bin/speedtest-cli && \  
mkdir -p /data && \  
useradd foo && \  
chown foo:foo /data  
  
RUN curl -Lo /nettests
https://github.com/e-minguez/nettests/releases/download/v0.0.1/nettests && \  
chmod a+x /nettests  
  
USER foo  
  
VOLUME /data  
  
CMD ["/nettests"]  

