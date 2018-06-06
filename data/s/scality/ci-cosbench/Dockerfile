# We use an Ubuntu OS because it is the reference OS in the COSBench
documentation.  
# We use the phusion passenger base image of Ubuntu, so that we can run
COSBench  
# as a multi-process container.  
FROM scality/nodesvc-base  
  
USER root  
  
ENV COSBENCH_VERSION="0.4.2.c2" COSBENCH_DIR="/tmp/cosbench"  
# Download and install Cosbench  
RUN apt-get update && \  
apt-get install openjdk-7-jre unzip curl -y --no-install-recommends && \  
curl --retry 6 \  
-Ls "https://github.com/intel-cloud/cosbench/releases/download/v${COSBENCH_VERSION}/${COSBENCH_VERSION}.zip" > /tmp/cosbench.zip && \  
cd /tmp ; unzip -q /tmp/cosbench.zip && \  
mv "/tmp/${COSBENCH_VERSION}" ${COSBENCH_DIR} && \  
rm /tmp/cosbench.zip && apt-get autoremove -y && \  
apt-get clean && chmod +x ${COSBENCH_DIR}/cli.sh  
  
COPY supervisord.conf ${COSBENCH_DIR}  
COPY controller.conf ${COSBENCH_DIR}/conf  
COPY driver.conf ${COSBENCH_DIR}/conf  
COPY driver_template.conf ${COSBENCH_DIR}/conf  
COPY scality-s3test-v1.1.xml.template ${COSBENCH_DIR}  
COPY run.sh /  
  
# COSBench driver port  
# COSBench controller port  
EXPOSE 18088 19088  
CMD cd ${COSBENCH_DIR} ; supervisord -c supervisord.conf  

