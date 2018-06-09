FROM alpine:3.6  
ENV ANSIBLE_VERSION v2.3.1.0-1  
ENV ANSIBLE_LINT 3.4.13  
ENV ANSIBLE_CLI 1.11.107  
ENV ANSIBLE_DIR /ansible  
ENV ANSIBLE_USER=ansible  
ENV ANSIBLE_HOME=/home/ansible  
ENV ANSIBLE_UID=10000  
ENV MANPATH=${ANSIBLE_DIR}/docs/man:  
ENV PATH=${ANSIBLE_DIR}/bin:${PATH}  
ENV PYTHONPATH=${ANSIBLE_DIR}/lib  
  
RUN apk add --no-cache bash \  
ca-certificates \  
git \  
openssh-client \  
openssl \  
py-crypto \  
py-jinja2 \  
py-markupsafe \  
py-paramiko \  
py-pip \  
py-setuptools \  
py-yaml \  
python \  
python-dev \  
tzdata \  
&& git clone https://github.com/ansible/ansible --branch "${ANSIBLE_VERSION}"
\--recursive --depth 1 "${ANSIBLE_DIR}" \  
&& cd "${ANSIBLE_DIR}" \  
&& mkdir -p /etc/ansible \  
&& echo localhost >> /etc/ansible/hosts \  
&& pip install ansible-lint==${ANSIBLE_LINT} \  
awscli==${ANSIBLE_CLI} \  
boto \  
boto3 \  
netaddr \  
requests \  
&& cp /usr/share/zoneinfo/Europe/London /etc/localtime \  
&& echo "Europe/London" > /etc/timezone \  
&& apk del tzdata python-dev \  
&& mkdir -p /root/.ssh \  
&& ssh-keyscan -H github.com >> /root/.ssh/known_hosts \  
&& adduser -h "${ANSIBLE_HOME}" -s /sbin/nologin -u "${ANSIBLE_UID}" -D
"${ANSIBLE_USER}" \  
&& echo chown -R "${ANSIBLE_USER}:${ANSIBLE_USER}" "${ANSIBLE_HOME}" \  
&& chown -R "${ANSIBLE_USER}:${ANSIBLE_USER}" "${ANSIBLE_HOME}"  
  
USER ${ANSIBLE_USER}  
WORKDIR ${ANSIBLE_HOME}  

