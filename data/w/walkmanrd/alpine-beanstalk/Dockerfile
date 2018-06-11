FROM alpine:latest  
MAINTAINER Dave Bevan <dockerfilemaintainer@tips1.co.uk>  
  
COPY alpine.patch /root/alpine.patch  
  
# Download and build beanstalk  
RUN buildDeps='gcc curl musl-dev make tar' \  
BEANSTALK_DOWNLOAD_URL="https://github.com/kr/beanstalkd/archive/v1.10.tar.gz"
\  
BEANSTALK_DOWNLOAD_SHA1="bfc0ccf99e15b15eac03ec1d8a57a3aaff143237" \  
&& set -x \  
&& addgroup beanstalk \  
&& adduser -H -D -s /bin/false -G beanstalk beanstalk \  
&& apk add --update $buildDeps \  
&& curl -sSL "$BEANSTALK_DOWNLOAD_URL" -o /tmp/beanstalk.tar.gz \  
&& mkdir -p /root/beanstalk \  
&& tar -xzf /tmp/beanstalk.tar.gz -C /root/beanstalk --strip-components=1 \  
&& rm -f /tmp/beanstalk.tar.gz \  
&& cd /root/beanstalk \  
&& patch -p0 < /root/alpine.patch \  
&& make \  
&& cd \  
&& mkdir -p /opt/beanstalk \  
&& cp /root/beanstalk/beanstalkd /opt/beanstalk \  
&& rm -rf /root/alpine.patch /root/beanstalk \  
&& apk del $buildDeps \  
&& rm -rf /var/cache/apk/* \  
;  
  
# the std beanstalkd port  
EXPOSE 11300  
  
# our start script - required to successfully trap SIGTERM (docker stop)  
COPY run.sh /run.sh  
  
# Auto-start the beanstalkd daemon. To run in verbose mode, start your docker  
# container as follows:  
#  
# docker start -p 11300:11300 -ti bevand10/alpine-beanstalk ./run.sh -V  
#  
CMD ["/run.sh"]  

