FROM alpine  
  
RUN apk add --update groff less python py-pip \  
&& pip install awscli \  
&& apk --purge -v del py-pip \  
&& rm -rf /var/cache/apk/*  
  
COPY entrypoint /  
ENV HOME /tmp  
ENV AWS_ACCESS_KEY_ID ""  
ENV AWS_SECRET_ACCESS_KEY ""  
ENV MAX_CONCURRENT_REQUESTS 10  
VOLUME $HOME/.aws/  
  
ENTRYPOINT ["/entrypoint"]  

