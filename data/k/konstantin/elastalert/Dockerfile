FROM python:2.7.14-alpine3.6  
ARG build_date  
ARG elastalert_version  
  
RUN apk add --no-cache --virtual .build-dependencies \  
gcc \  
libffi-dev \  
make \  
musl-dev \  
openssl-dev \  
python2-dev \  
&& pip install --upgrade pip \  
&& pip install \  
elastalert==$elastalert_version \  
&& apk del .build-dependencies  
  
LABEL org.label-schema.schema-version=1.0  
LABEL org.label-schema.build-date=$build_date  
LABEL org.label-schema.name=elastalert  
LABEL org.label-schema.description="Easy & Flexible Alerting With
ElasticSearch"  
LABEL org.label-schema.url="https://elastalert.readthedocs.io/"  
LABEL org.label-schema.vcs-url="https://github.com/Yelp/elastalert"  
LABEL org.label-schema.version=$elastalert_version  
LABEL org.label-schema.vendor=konstantin  
LABEL org.label-schema.docker.cmd="docker run --rm --volume
$PWD:/etc/elastalert:ro --name elastalert
konstantin/elastalert:$elastalert_version"  
  
VOLUME ["/etc/elastalert"]  
WORKDIR "/etc/elastalert"  
  
CMD ["elastalert"]  

