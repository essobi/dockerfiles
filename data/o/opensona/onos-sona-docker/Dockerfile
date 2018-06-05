# First stage is the build environment  
FROM opensona/centos-oracle-java:jdk8 as builder  
MAINTAINER Jian Li <gunine@sk.com>  
  
# Set the environment variables  
ENV HOME /root  
ENV BUILD_NUMBER docker  
ENV JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8  
  
# Install dependencies  
RUN yum install -y git  
  
# Copy in the source  
RUN git clone \--branch 1.13.1 https://github.com/opennetworkinglab/onos.git
onos  
RUN mkdir -p /src/  
RUN cp -R onos /src/  
  
# Build ONOS  
# We extract the tar in the build environment to avoid having to put the tar  
# in the runtime environment - this saves a lot of space  
# FIXME - dependence on ONOS_ROOT and git at build time is a hack to work
around  
# build problems  
WORKDIR /src/onos  
RUN yum install -y zip unzip which python bzip2 && \  
export ONOS_ROOT=/src/onos && \  
tools/build/onos-buck build onos && \  
mkdir -p /src/tar && \  
cd /src/tar && \  
tar -xf /src/onos/buck-out/gen/tools/package/onos-package/onos.tar.gz --strip-
components=1 && \  
rm -rf /src/onos/buck-out .git  
  
# Second stage is the runtime environment  
FROM gunine/centos-oracle-java:server-jre8  
  
# Change to /root directory  
RUN yum install -y curl && \  
mkdir -p /root/onos  
WORKDIR /root/onos  
  
# Install ONOS  
COPY \--from=builder /src/tar/ .  
  
# Configure ONOS to log to stdout  
RUN sed -ibak '/log4j.rootLogger=/s/$/, stdout/' $(ls -d apache-
karaf-*)/etc/org.ops4j.pax.logging.cfg  
  
LABEL org.label-schema.name="ONOS" \  
org.label-schema.description="SDN Controller" \  
org.label-schema.usage="http://wiki.onosproject.org" \  
org.label-schema.url="http://onosproject.org" \  
org.label-scheme.vendor="Open Networking Foundation" \  
org.label-schema.schema-version="1.0"  
  
RUN touch apps/org.onosproject.drivers/active && \  
touch apps/org.onosproject.openflow-base/active && \  
touch apps/org.onosproject.openstacknetworking/active  
  
# Ports  
# 6653 - OpenFlow  
# 6640 - OVSDB  
# 8181 - GUI  
# 8101 - ONOS CLI  
# 9876 - ONOS intra-cluster communication  
EXPOSE 6653 6640 8181 8101 9876  
# Get ready to run command  
ENTRYPOINT ["./bin/onos-service"]  
CMD ["server"]  

