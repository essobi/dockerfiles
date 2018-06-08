FROM alpine:3.6  
  
LABEL Name=molecule Version=0.0.1  
  
ENV DOCKER_COMPOSE_VERSION=1.16.0  
ENV ANSIBLE_VERSION=2.4.0.0  
ENV MOLECULE_VERSION=2.3.0  
ENV ENTRYKIT_VERSION=0.4.0  
ENV PORT=1337  
  
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories \  
&& apk --update --no-cache add \  
aufs-util \  
bash \  
ca-certificates \  
curl \  
device-mapper \  
docker \  
git \  
iptables \  
python2 \  
py-pip \  
rsyslog \  
&& apk --update --no-cache add --virtual \  
build-dependencies \  
build-base \  
libffi-dev \  
linux-headers \  
openssl-dev \  
python2-dev \  
&& pip install --no-cache-dir --upgrade \  
pip \  
cffi \  
&& pip install --no-cache-dir \  
ansible==${ANSIBLE_VERSION} \  
boto \  
boto3 \  
docker-compose==${DOCKER_COMPOSE_VERSION} \  
docker-py \  
dopy \  
molecule==${MOLECULE_VERSION} \  
&& curl -L
https://github.com/progrium/entrykit/releases/download/v${ENTRYKIT_VERSION}/entrykit_${ENTRYKIT_VERSION}_Linux_x86_64.tgz
| tar zx \  
&& chmod +x entrykit \  
&& mv entrykit /bin/entrykit \  
&& entrykit --symlink \  
&& apk del build-dependencies \  
&& rm -rf /var/cache/apk/*  
  
# Include useful functions to start/stop docker daemon in garden-runc
containers in Concourse CI.  
# Example: source /docker-lib.sh && start_docker  
ADD ./docker-lib.sh /usr/local/bin/docker-lib.sh  
  
ENTRYPOINT [ \  
"switch", \  
"shell=/bin/sh", "--", \  
"codep", \  
"/usr/bin/dockerd", \  
"/usr/sbin/rsyslogd" \  
]  

