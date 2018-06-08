# BUILD  
# =====  
FROM ubuntu:xenial as buildstep  
LABEL maintainer="Hans Lellelid <hans@xmpl.org>"  
  
RUN apt-get update && apt-get install -y software-properties-common build-
essential git curl  
  
ENV BEANSTALKD_VERSION="1.10"  
RUN curl -sL
https://github.com/kr/beanstalkd/archive/v${BEANSTALKD_VERSION}.tar.gz | tar
xvz -C /tmp  
  
WORKDIR /tmp/beanstalkd-${BEANSTALKD_VERSION}  
RUN make  
RUN cp beanstalkd /tmp/  
  
# DEPLOY  
# =====  
FROM ubuntu:xenial as deploystep  
LABEL maintainer="Hans Lellelid <hans@xmpl.org>"  
  
COPY \--from=buildstep /tmp/beanstalkd /usr/bin/beanstalkd  
  
RUN mkdir -p /data  
VOLUME /data  
  
EXPOSE 11300  
CMD ["beanstalkd", "-p", "11300", "-b", "/data", "-f", "5000", "-V"]

