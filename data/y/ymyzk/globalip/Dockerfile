FROM alpine:latest  
  
MAINTAINER Yusuke Miyazaki <miyazaki.dev@gmail.com>  
  
RUN apk add --no-cache curl jq python  
  
WORKDIR /root  
  
RUN curl -s -o sdk.tar.gz
https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-130.0.0-linux-x86_64.tar.gz \  
&& tar xzf sdk.tar.gz \  
&& rm sdk.tar.gz \  
&& ./google-cloud-sdk/install.sh \  
&& ./google-cloud-sdk/bin/gcloud components update  
  
COPY ./insert.sh /root/  
COPY ./start.sh /root/  
  
ENV GCLOUD_KEY_FILE /root/gcloud_key.json  
ENV CRONTAB_TIME */15 * * * *  
  
CMD ["./start.sh"]  

