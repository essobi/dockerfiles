# First stage is the build environment  
FROM sgrio/java-oracle:jdk_8 as builder  
MAINTAINER Jian Li <gunine@sk.com>  
  
# Set the environment variables  
ENV HOME /root  
ENV BUILD_NUMBER docker  
ENV JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8  
ENV ONOS_VERSION 1.13.1  
# Install dependencies  
RUN apt-get update && apt-get install -y git  
  
# Copy in the source  
RUN git clone \--branch ${ONOS_VERSION} https://gerrit.onosproject.org/onos
onos  
RUN mkdir -p /src/  
RUN cp -R onos /src/  
  
# Remove SONA apps sources  
RUN rm -rf /src/onos/apps/openstacknetworking  
RUN rm -rf /src/onos/apps/openstacknode  
RUN rm -rf /src/onos/apps/openstacknetworkingui  
  
# Download and patch ONOS core changes which affect ONOS  
RUN git clone https://github.com/sonaproject/onos-sona-patch.git patch  
RUN cp patch/${ONOS_VERSION}/*.patch /src/onos/  
RUN cp patch/patch.sh /src/onos/  
WORKDIR /src/onos  
RUN ./patch.sh  
  
# Download latest SONA app sources  
WORKDIR /onos  
RUN git checkout master  
RUN cp -R apps/openstacknetworking ../src/onos/apps  
RUN cp -R apps/openstacknode ../src/onos/apps  
RUN cp -R apps/openstacknetworkingui ../src/onos/apps  
  
# Build ONOS  
# We extract the tar in the build environment to avoid having to put the tar  
# in the runtime environment - this saves a lot of space  
# FIXME - dependence on ONOS_ROOT and git at build time is a hack to work
around  
# build problems  
WORKDIR /src/onos  
RUN apt-get update && apt-get install -y zip python git bzip2 && \  
export ONOS_ROOT=/src/onos && \  
tools/build/onos-buck build onos && \  
mkdir -p /src/tar && \  
cd /src/tar && \  
tar -xf /src/onos/buck-out/gen/tools/package/onos-package/onos.tar.gz --strip-
components=1 && \  
rm -rf /src/onos/buck-out .git  
  
# Second stage is the runtime environment  
FROM anapsix/alpine-java:8_server-jre  
  
# Change to /root directory  
RUN apk update && \  
apk add curl && \  
mkdir -p /root/onos  
  
WORKDIR /root  
COPY bash_profile .bash_profile  
  
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

