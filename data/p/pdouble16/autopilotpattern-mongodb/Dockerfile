FROM pdouble16/autopilotpattern-base:1.2.0  
FROM golang:1.8.5  
WORKDIR /go/src/github.com/percona  
RUN git clone https://github.com/percona/mongodb_exporter.git  
WORKDIR /go/src/github.com/percona/mongodb_exporter  
RUN git checkout tags/v0.4.0  
RUN go get github.com/kardianos/govendor  
RUN govendor sync  
RUN go build -o mongodb_exporter github.com/percona/mongodb_exporter  
  
FROM mongo:3.7.9  
ARG BUILD_DATE  
ARG SOURCE_TYPE  
ARG SOURCE_REF  
ARG DOCKERFILE_PATH  
  
RUN mkdir -p /var/lib/consul /etc/consul  
COPY \--from=0 /usr/local/bin/* /usr/local/bin/  
COPY \--from=0 /etc/consul/* /etc/consul/  
  
ENV CONTAINERPILOT="/etc/containerpilot.json5" \  
PYTHONOPTIMIZE=x \  
# add stopping timeouts for MongoDB  
MONGO_SECONDARY_CATCHUP_PERIOD=8 \  
MONGO_STEPDOWN_TIME=60 \  
MONGO_ELECTION_TIMEOUT=30 \  
MONGO_REPLSET=joyent  
  
RUN apt-get update \  
&& apt-get install -y \  
python \  
python-dev \  
gcc \  
curl \  
libffi-dev \  
libssl-dev \  
unzip \  
jq \  
# get Python drivers MongoDB, Consul, and Manta  
&& curl -Ls -o /tmp/get-pip.py https://bootstrap.pypa.io/get-pip.py \  
&& python /tmp/get-pip.py \  
&& pip install --compile \  
PyMongo==3.6.1 \  
python-Consul==1.0.1 \  
manta==2.6.1 \  
awscli==1.15.26 \  
azure-cli-storage==2.0.33 \  
gcs-client==0.2.2 \  
mock==2.0.0 \  
&& apt-get purge -y --auto-remove gcc libffi-dev libssl-dev python-dev \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
COPY \--from=1 /go/src/github.com/percona/mongodb_exporter/mongodb_exporter
/usr/local/bin/mongodb_exporter  
  
COPY etc/containerpilot.json5 ${CONTAINERPILOT}  
COPY bin/* /usr/local/bin/  
  
VOLUME [ "/seed" ]  
CMD ["/usr/local/bin/containerpilot"]  
  
HEALTHCHECK \--interval=60s --timeout=10s --retries=3 CMD
["/usr/local/bin/consul-manage", "health"] || exit 1  
  
LABEL maintainer="Patrick Double <pat@patdouble.com>" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.license="MPL-2.0" \  
org.label-schema.vendor="https://bitbucket.org/double16" \  
org.label-schema.name="Autopilot MongoDB with Prometheus Monitoring" \  
org.label-schema.url="https://bitbucket.org/double16/autopilotpattern-mongodb"
\  
org.label-schema.docker.dockerfile="${DOCKERFILE_PATH}/Dockerfile" \  
org.label-schema.vcs-ref=$SOURCE_REF \  
org.label-schema.vcs-type=${SOURCE_TYPE} \  
org.label-schema.vcs-url="https://bitbucket.org/double16/autopilotpattern-
mongodb.git"  

