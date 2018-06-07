FROM alpine:3.3  
RUN apk --update add \  
python \  
py-pip \  
&& pip install boto3 \  
&& apk del py-pip \  
&& rm -rf /var/cache/apk/* \  
&& mkdir /app  
  
WORKDIR /app  
  
ADD asg_persistence/ /app  
  
CMD python

