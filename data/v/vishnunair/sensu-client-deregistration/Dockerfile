From alpine:edge  
MAINTAINER Vishnu Nair <me@vishnudxb.me>  
  
ENV aws_access_key_id=aws_access_key_id  
ENV aws_secret_access_key=aws_secret_access_key  
ENV region=region  
ENV sensu_master=sensu_master  
ENV aws_instance_tag=aws_instance_tag  
ENV ip_regex=ip_regex  
  
  
RUN apk add \--update curl python python-dev py-pip build-base py-setuptools
jq && pip install awscli setuptools httpie && mkdir -p /src/ /root/.aws  
WORKDIR /src  
COPY aws/config /root/.aws/credentials  
COPY sensu-client-removal.sh /sensu-client-removal.sh  
RUN chmod +x /sensu-client-removal.sh  
ADD crontab /var/spool/cron/crontabs/root  
  
CMD crond -f  

