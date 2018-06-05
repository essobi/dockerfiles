# Stage 1  
FROM python:rc-alpine  
MAINTAINER infrastructure@dallasmakerspace.org  
  
COPY . /data/  
WORKDIR /data  
  
# Needed to reach the hub and pypi  
RUN apk --no-cache add make curl ca-certificates \  
&& curl -sL https://github.com/openfaas/faas/releases/download/0.7.1/fwatchdog
> /usr/bin/fwatchdog \  
&& chmod +x /usr/bin/fwatchdog /data/*.py \  
&& pip install -r /data/requirements.txt  
  
EXPOSE 8080  
ENV VIRTUAL_PORT 8080  
ENV fprocess "/usr/bin/env python /data/member-storage-audit.py"  
HEALTHCHECK \--interval=5s CMD [ -e /tmp/.lock ] || exit 1  
CMD ["/usr/bin/fwatchdog"]  

