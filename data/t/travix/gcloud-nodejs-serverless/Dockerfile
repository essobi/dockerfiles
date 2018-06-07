FROM travix/alpine-gcloud:168.0.0  
  
ENV CLOUDSDK_CORE_DISABLE_PROMPTS=1  
  
RUN apk add --update --no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/main/ --allow-untrusted \  
nodejs>6.9.5-r1 \  
nodejs-npm \  
&& apk add --update --no-cache \  
git \  
libc6-compat \  
make \  
&& npm i -g serverless \  
&& gcloud components update \  
&& gcloud components remove bq \  
&& rm -rf google-cloud-sdk/.install/.backup \  
&& rm -rf google-cloud-sdk/.install/.download \  
&& rm -rf /var/cache/apk/*  

