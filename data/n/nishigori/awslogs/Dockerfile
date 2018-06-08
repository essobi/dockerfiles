FROM python:3-alpine  
  
RUN set -x \  
&& apk upgrade --no-cache \  
&& apk add --no-cache coreutils bash tzdata jq \  
&& cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \  
&& apk del tzdata \  
&& rm -rf /var/cache/apk/*  
  
# https://pypi.python.org/pypi/awslogs/  
ENV AWSLOGS_VER 0.10.0  
RUN pip install --no-cache-dir awslogs==$AWSLOGS_VER  
  
ENTRYPOINT ["awslogs"]  
CMD []  

