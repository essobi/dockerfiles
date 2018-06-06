FROM cogentwebs/base  
MAINTAINER Pichate Ins <cogent@cogentwebworks.com>  
  
# Set labels  
LABEL com.ansible.cogentwebworks.version="0.0.1-beta"  
  
# ROOTFS  
COPY rootfs /  
  
RUN addgroup -g 82 -S sysansible && adduser -u 82 -D -S -G sysansible
sysansible  
# Install ansible  
RUN apk-install --update sudo python py-pip openssl ca-certificates && \  
apk --update add --virtual build-dependencies python-dev libffi-dev openssl-
dev build-base && \  
pip install --upgrade pip cffi && \  
pip install ansible pywinrm && apk del build-dependencies && \  
mkdir -p /etc/ansible && \  
echo "localhost ansible_connection=local" > /etc/ansible/hosts && apk-clean  
  
#EXPOSE 80 443 2015  
#VOLUME  
VOLUME ["/usr/local/data"]  
# INIT S6  
ENTRYPOINT ["/init"]

