FROM infotechsoft/htcondor:8.6  
ARG PEGASUS_VERSION=4.8.1  
ENV PEGASUS_VERSION $PEGASUS_VERSION  
ENV PEGASUS_SERVER_HOST localhost  
ENV PEGASUS_SERVER_PORT 5000  
LABEL name="infotechsoft/pegasus" \  
vendor="INFOTECH Soft, Inc." \  
version="${PEGASUS_VERSION}" \  
release-date="2018-01-17" \  
maintainer="Thomas J. Taylor <thomas@infotechsoft.com>"  
# Pegasus-WMS  
RUN curl -o /etc/yum.repos.d/pegasus.repo
https://download.pegasus.isi.edu/wms/download/rhel/7/pegasus.repo && \  
yum -y install pegasus-${PEGASUS_VERSION} && \  
yum -y clean all  
  
RUN export PYTHONPATH=`pegasus-config --python` && \  
export PERL5LIB=`pegasus-config --perl` && \  
export CLASSPATH=`pegasus-config --classpath`  
  
EXPOSE $PEGASUS_SERVER_PORT  
  
CMD condor_master -f -t & && \  
pegasus-service --host $PEGASUS_SERVER_HOST --port $PEGASUS_SERVER_PORT

