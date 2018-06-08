FROM alpine:3.4  
MAINTAINER Benjamin Pannell <admin@sierrasoftworks.com>  
  
RUN set -ex \  
&& apk --update add sudo \  
&& apk --update add python py-pip openssl ca-certificates \  
&& apk --update add --virtual build-dependencies python-dev libffi-dev
openssl-dev build-base \  
&& pip install --upgrade pip cffi \  
&& pip install ansible \  
&& apk del build-dependencies \  
&& rm -rf /var/cache/apk/* \  
&& mkdir -p /etc/ansible \  
&& echo 'localhost' > /etc/ansible/hosts  
  
WORKDIR /ansible  
VOLUME /ansible  
  
CMD ["ansible", "--version"]

