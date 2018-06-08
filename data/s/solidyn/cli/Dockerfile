FROM alpine:3.6  
  
LABEL maintainer='Ian Martin <imartin@solidyn.com>' license='MIT' name='CLI'\  
description='All the CLIs, all in one place'
url='https://github.com/solidyn/docker' \  
vendor='Solidyn Solutions' version='1.0'  
  
# installs AWS, PCF and OpenShift CLI's  
RUN apk -Uuv add groff less python py-pip tar gzip curl postgresql-client
mysql-client && \  
pip install awscli aws-amicleaner && \  
curl -skL
'https://cli.run.pivotal.io/stable?release=linux64-binary&source=github' | tar
-xz && \  
mv cf /bin/cf && \  
chmod 755 /bin/cf && \  
curl -skL
'https://github.com/openshift/origin/releases/download/v3.6.1/openshift-
origin-client-tools-v3.6.1-008f2d5-linux-64bit.tar.gz' | tar -xz --strip-
components=1 && \  
mv oc /bin/oc && \  
curl -skL https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64
-o /usr/bin/jq && \  
chown root:root /usr/bin/jq && \  
chmod 755 /usr/bin/jq && \  
rm /var/cache/apk/* && \  
addgroup -g 8728 cli && \  
adduser -D -u 8728 -G cli cli && \  
mkdir -p /data && \  
chown -R cli:root /data  
  
USER cli  
VOLUME ["/data"]  
WORKDIR /data  

