FROM python:3.6.4-alpine3.7  
LABEL maintainer="Ben Jones <ben@fogbutter.com>"  
  
ARG BOTO3_VERSION=1.6.3  
ARG BOTOCORE_VERSION=1.9.3  
ARG APPUSER=app  
ARG PROJECTDIR=/home/${APPUSER}/project  
  
RUN addgroup ${APPUSER} && adduser -S app -G app && \  
apk add --update-cache make && \  
apk add --virtual .build-deps gcc \  
musl-dev \  
linux-headers \  
libffi-dev \  
openssl-dev && \  
pip install --upgrade pip && \  
pip install --no-cache-dir botocore==${BOTOCORE_VERSION} \  
boto3==${BOTO3_VERSION} && \  
mkdir /python-testing && \  
pip install --no-cache-dir \  
\--prefix /python-testing \  
botocore==${BOTOCORE_VERSION} \  
boto3==${BOTO3_VERSION} \  
pytest \  
pytest-cov \  
moto && \  
apk del .build-deps && rm -rf /var/cache/apk/* && \  
mkdir -p ${PROJECTDIR} && chown ${APPUSER}:${APPUSER} ${PROJECTDIR}  
  
WORKDIR ${PROJECTDIR}  
USER app  

