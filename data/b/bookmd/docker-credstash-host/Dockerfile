FROM alpine:latest  
  
# adapted from macropin/sshd  
  
MAINTAINER BookMD  
  
RUN apk add --update \  
bash \  
build-base \  
libffi-dev \  
openssh \  
openssl-dev \  
python-dev \  
py-pip \  
&& pip install --upgrade pip \  
&& mkdir -p ~root/.ssh /etc/authorized_keys && chmod 700 ~root/.ssh/ \  
&& echo -e "AuthorizedKeysFile\t.ssh/authorized_keys /etc/authorized_keys/%u"
>> /etc/ssh/sshd_config \  
&& pip install awscli \  
&& pip install credstash \  
&& rm -rf /var/cache/apk/*  
  
COPY entry.sh /entry.sh  
ENTRYPOINT ["/entry.sh"]  
  
CMD ["/usr/sbin/sshd", "-D", "-f", "/etc/ssh/sshd_config"]

