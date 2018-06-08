FROM python:2-alpine  
MAINTAINER Elliot Wright <hello@elliotdwright.com>  
  
RUN set -x \  
&& pip install --upgrade awscli \  
&& mkdir -p /root/.aws \  
&& chmod 700 /root/.aws  
  
VOLUME /root/.aws  
  
ENTRYPOINT ["aws"]  
  
CMD ["--version"]  

