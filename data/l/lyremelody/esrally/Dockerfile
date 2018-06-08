FROM python:3.6.4-alpine3.6  
LABEL maintainer "https://github.com/lyremelody"  
  
ENV TARGET_HOST="elasticseach.host:9200"  
ENV REPORT_FORMAT="markdown"  
ENV TRACK="geopoint"  
RUN apk add --update --no-cache --no-install-recommends git build-base linux-
headers python-dev && rm -rf /var/lib/apt/lists/*  
RUN pip install esrally==0.9.0  
  
COPY rally.ini /root/.rally/  
  
CMD esrally --pipeline=benchmark-only --target-hosts=$TARGET_HOST
\--track=$TRACK \--report-format=$REPORT_FORMAT  
  

