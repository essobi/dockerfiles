FROM python:3-alpine  
  
LABEL maintainer Jiayu Liu <etareduce@gmail.com>  
  
# explicitly set user/group IDs  
RUN addgroup -g 896 -S luigid && adduser -D -u 896 -S -G luigid luigid  
  
RUN apk add --no-cache \  
'su-exec>=0.2' \  
libpq \  
postgresql-dev \  
musl-dev \  
gcc  
  
ADD requirements.txt /tmp/requirements.txt  
  
RUN pip install -r /tmp/requirements.txt  
  
WORKDIR /etc/luigi  
  
ADD client.cfg /etc/luigi/client.cfg  
  
EXPOSE 8082  
CMD ["su-exec", "luigid", "/usr/local/bin/luigid"]  

