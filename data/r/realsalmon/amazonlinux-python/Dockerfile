FROM amazonlinux:2017.03.1.20170812  
LABEL maintainer="Ben Jones <ben@fogbutter.com>"  
ARG PYTHON_VERSION=3.6.4  
ARG BOTO3_VERSION=1.6.3  
ARG BOTOCORE_VERSION=1.9.3  
ARG APPUSER=app  
  
COPY entrypoint.sh /entrypoint.sh  
RUN yum -y update &&\  
yum install -y shadow-utils findutils gcc sqlite-devel zlib-devel \  
bzip2-devel openssl-devel readline-devel libffi-devel && \  
groupadd ${APPUSER} && useradd ${APPUSER} -g ${APPUSER} && \  
cd /usr/local/src && \  
curl -O
https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz
&& \  
tar -xzf Python-${PYTHON_VERSION}.tgz && \  
cd Python-${PYTHON_VERSION} && \  
./configure --enable-optimizations && make && make altinstall && \  
chmod +x /entrypoint.sh && \  
rm -rf /usr/local/src/Python-${PYTHON_VERSION}* && \  
yum remove -y shadow-utils audit-libs libcap-ng && yum -y autoremove && \  
yum clean all  
  
USER ${APPUSER}  
RUN python3.6 -m venv /home/${APPUSER}/venv && \  
source /home/${APPUSER}/venv/bin/activate && \  
pip install --upgrade pip && \  
mkdir -p /home/${APPUSER}/python-testing \  
/home/${APPUSER}/bin \  
/home/${APPUSER}/project && \  
pip install --no-cache boto3==${BOTO3_VERSION} \  
botocore==${BOTOCORE_VERSION} && \  
pip install --no-cache -t /home/${APPUSER}/python-testing \  
\--install-option="--install-scripts=/home/${APPUSER}/bin" \  
boto3==${BOTO3_VERSION} \  
botocore==${BOTOCORE_VERSION} \  
pytest \  
pytest-cov \  
moto  
  
WORKDIR /home/${APPUSER}/project  
ENTRYPOINT ["/entrypoint.sh"]  

