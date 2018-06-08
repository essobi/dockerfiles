FROM dweinstein/androguard:v2.0.0  
MAINTAINER dweinstein "dweinst@insitusec.com"  
ADD https://github.com/dweinstein/analysis-runner/archive/v3.0.0.zip
/tmp/runner.zip  
RUN unzip -j /tmp/runner.zip -d /opt/runner && \  
rm -f /tmp/runner.zip  
  
WORKDIR /opt/androguard-manifest/  
ADD ./androguard_manifest.py /opt/androguard-manifest/androguard_manifest.py  
ENV TOOL ${PYTHON} ./androguard_manifest.py  
ENV CONTENT_TYPE text/xml  
  
ENTRYPOINT ["/opt/runner/runner.sh", "${TOOL}"]  
  

