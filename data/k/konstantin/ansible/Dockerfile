ARG alpine_version=3.6  
FROM alpine:${alpine_version}  
  
ARG ansible_version  
ARG build_date  
  
RUN apk add --no-cache \  
ca-certificates \  
openssh-client \  
openssl \  
py-pip \  
python \  
sshpass \  
&& apk add --no-cache --virtual .build-dependencies \  
gcc \  
libffi-dev \  
make \  
musl-dev \  
openssl-dev \  
python-dev \  
&& pip install --upgrade pip \  
&& pip install \  
ansible==$ansible_version \  
&& apk del .build-dependencies  
  
LABEL org.label-schema.schema-version=1.0  
LABEL org.label-schema.build-date=$build_date  
LABEL org.label-schema.name=ansible  
LABEL org.label-schema.description="Radically simple IT automation"  
LABEL org.label-schema.url="https://www.ansible.com/"  
LABEL org.label-schema.vcs-url="https://github.com/ansible/ansible"  
LABEL org.label-schema.version=$ansible_version  
LABEL org.label-schema.vendor=konstantin  
LABEL org.label-schema.docker.cmd="docker run --rm
konstantin/ansible:$version-alpine$alpine_version ansible --version"  

