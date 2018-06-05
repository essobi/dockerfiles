FROM python:2-alpine  
MAINTAINER Simon Erhardt <me+docker@rootlogin.ch>  
  
ENV AGE=24 \  
AT_AGE=24 \  
PER_PAGE=150 \  
MAX_PAGE=5 \  
USE_LIMIT=0.25 \  
EVERY=60 \  
EXCLUDE="[\"\"]" \  
CONSUMER_KEY=null \  
CONSUMER_SECRET=null \  
ACCESS_TOKEN=null \  
ACCESS_SECRET=null  
  
RUN apk add --update \  
git \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir -p /opt/twdlt  
  
COPY run.sh /opt/twdlt/run.sh  
RUN chmod +x /opt/twdlt/run.sh  
  
RUN git clone https://github.com/YoSmudge/twdlt.git /opt/twdlt/src  
RUN cd /opt/twdlt/src && pip install -r requirements.txt  
  
CMD ["/opt/twdlt/run.sh"]  

