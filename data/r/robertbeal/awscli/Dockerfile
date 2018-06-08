FROM alpine:3.6  
  
RUN addgroup -S awscli && adduser -h /data -G awscli -S awscli  
  
RUN apk --no-cache add \  
python \  
py-pip \  
groff \  
less \  
&& pip install awscli==1.11.129 \  
&& apk del --purge py-pip  
  
USER awscli  
ENTRYPOINT ["aws"]  

