FROM alpine:3.6  
MAINTAINER Andrey Sizov <andrey.sizov@jetbrains.com>  
  
# Versions: https://pypi.python.org/pypi/awscli#downloads  
ENV AWS_CLI_VERSION=1.11.131 \  
RCLONE_VERSION=current \  
ARCH=amd64  
  
RUN apk --no-cache update && \  
apk --no-cache add python py-pip py-setuptools ca-certificates groff less jq
wget openssl && \  
update-ca-certificates && \  
pip --no-cache-dir install awscli==${AWS_CLI_VERSION} && \  
rm -rf /var/cache/apk/* && \  
cd /tmp && \  
wget -q http://downloads.rclone.org/rclone-${RCLONE_VERSION}-linux-${ARCH}.zip
&& \  
unzip /tmp/rclone-${RCLONE_VERSION}-linux-${ARCH}.zip && \  
mv /tmp/rclone-*-linux-${ARCH}/rclone /usr/bin && \  
rm -r /tmp/rclone*  
  
COPY run.sh s3-lifecycle.json /  
RUN chmod a+x /run.sh  
  
WORKDIR /data  
  
CMD ["/run.sh"]

