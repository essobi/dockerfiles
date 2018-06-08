FROM alpine  
MAINTAINER yikaus  
  
RUN set -ex \  
&& apk add --no-cache py-pip build-base python-dev libffi-dev openssl-dev \  
&& pip install ansible \  
&& mkdir /ansible \  
&& apk del build-base py-pip libffi-dev openssl-dev  
  
WORKDIR /ansible  
  
ENTRYPOINT ["ansible-playbook"]

