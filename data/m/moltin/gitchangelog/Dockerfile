FROM python:alpine  
MAINTAINER Israel Sotomayor <israel@moltin.com>  
  
COPY ./requirements.txt /tmp/requirements.txt  
  
RUN set -x \  
&& apk --no-cache add \  
git \  
ca-certificates \  
\  
&& cd /tmp \  
&& pip install -r requirements.txt \  
\  
&& rm -rf /tmp/requirements.txt  
  
RUN mkdir /code  
WORKDIR /code  
  
CMD ["gitchangelog"]  

