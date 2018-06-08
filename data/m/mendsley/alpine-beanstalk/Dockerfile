FROM alpine:3.4  
MAINTAINER Matthew Endsley <mendsley@gmail.com>  
  
COPY alpine.patch /root/alpine.patch  
  
# Download and build beanstalk  
RUN buildDeps='gcc curl musl-dev make tar' \  
BEANSTALK_DOWNLOAD_URL="https://github.com/kr/beanstalkd/archive/v1.10.tar.gz"
\  
BEANSTALK_DOWNLOAD_SHA1="bfc0ccf99e15b15eac03ec1d8a57a3aaff143237" \  
&& set -x \  
&& addgroup beanstalk \  
&& adduser -H -D -s /bin/false -G beanstalk beanstalk \  
&& apk add --no-cache $buildDeps \  
&& curl -sSL "$BEANSTALK_DOWNLOAD_URL" -o /tmp/beanstalk.tar.gz \  
&& mkdir -p /root/beanstalk \  
&& tar -xzf /tmp/beanstalk.tar.gz -C /root/beanstalk --strip-components=1 \  
&& rm -f /tmp/beanstalk.tar.gz \  
&& cd /root/beanstalk \  
&& patch -p0 < /root/alpine.patch \  
&& make \  
&& cd \  
&& cp /root/beanstalk/beanstalkd /usr/local/bin/ \  
&& rm -rf /root/alpine.patch /root/beanstalk \  
&& apk del $buildDeps \  
;  

