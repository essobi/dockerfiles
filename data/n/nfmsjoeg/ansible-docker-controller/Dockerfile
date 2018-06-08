FROM alpine:latest  
  
ENV ANSIBLE_VERSION 2.5.0b2  
  
ENV BUILD_PACKAGES \  
bash \  
curl \  
tar \  
openssh-client \  
sshpass \  
git \  
python \  
py-boto \  
py-dateutil \  
py-httplib2 \  
py-jinja2 \  
py-paramiko \  
py-pip \  
py-setuptools \  
py-yaml \  
ca-certificates  
  
RUN apk --update add --virtual build-dependencies \  
gcc \  
musl-dev \  
libffi-dev \  
openssl-dev \  
python-dev  
  
RUN set -x && \  
apk update && apk upgrade && \  
apk add --no-cache ${BUILD_PACKAGES} && \  
pip install --upgrade pip && \  
pip install python-keyczar docker-py ansible==${ANSIBLE_VERSION} && \  
apk del build-dependencies && \  
rm -rf /var/cache/apk/*  
  
RUN mkdir -p /etc/ansible /ansible  
  
RUN echo "[local]" >> /etc/ansible/hosts && \  
echo "localhost" >> /etc/ansible/hosts  
  
ENV ANSIBLE_GATHERING smart  
ENV ANSIBLE_HOST_KEY_CHECKING false  
ENV ANSIBLE_RETRY_FILES_ENABLED false  
ENV ANSIBLE_ROLES_PATH /ansible/playbooks/roles  
ENV ANSIBLE_SSH_PIPELINING True  
ENV PYTHONPATH /ansible/lib  
ENV PATH /ansible/bin:$PATH  
ENV ANSIBLE_LIBRARY /ansible/library  
  
WORKDIR /ansible/playbooks  
  
ENTRYPOINT ["ansible-playbook"]  

