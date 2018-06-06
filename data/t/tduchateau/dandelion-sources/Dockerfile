# Dandelion sources 0.10.0 and examples  
FROM tduchateau/dandelion-base  
MAINTAINER Thibault Duchateau <thibault.duchateau@gmail.com>  
  
#  
# Download project sources  
#  
# Dandelion-Core  
RUN cd /home/dandelion && \  
git clone https://github.com/dandelion/dandelion.git dandelion-core && \  
cd dandelion-core && \  
git checkout tags/dandelion-0.10.0 && \  
chown -R dandelion:dandelion /home/dandelion  
  
# Dandelion-Datatables  
RUN cd /home/dandelion && \  
git clone https://github.com/dandelion/dandelion-datatables.git dandelion-
datatables && \  
cd dandelion-datatables && \  
git checkout tags/dandelion-datatables-0.10.0 && \  
chown -R dandelion:dandelion /home/dandelion  
  
# Dandelion-Samples  
RUN cd /home/dandelion && \  
git clone https://github.com/dandelion/dandelion-samples.git dandelion-samples
&& \  
cd dandelion-samples && \  
git checkout tags/samples-0.10.0 && \  
chown -R dandelion:dandelion /home/dandelion  
  
#  
# Build and install in the Maven local repository  
#  
# Dandelion-Core  
RUN cd /home/dandelion/dandelion-core && \  
mvn clean install  
  
# Dandelion-Datatables  
RUN cd /home/dandelion/dandelion-datatables && \  
mvn clean install  
  
# Expose the Tomcat port  
EXPOSE 9090

