FROM alpine:3.5  
  
RUN set -x \  
&& apk add --no-cache \  
ca-certificates \  
duplicity \  
lftp \  
openssh \  
openssl \  
py-crypto \  
py-pip \  
py-paramiko \  
py-setuptools \  
rsync \  
&& update-ca-certificates \  
&& pip install pydrive==1.3.1 \  
&& apk del --purge py-pip \  
&& mkdir -p /root/.cache/duplicity \  
&& mkdir -p /root/.gnupg \  
&& chmod -R go+rwx /root  
  
ENV HOME=/root  
  
VOLUME ["/root/.cache/duplicity", "/root/.gnupg"]  
  
ENTRYPOINT ["duplicity"]  

