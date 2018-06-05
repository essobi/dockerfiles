FROM alpine:3.7  
ENV AWSCLI_VERSION "1.14.30"  
RUN apk --update add --no-cache \  
git \  
python \  
py-pip \  
groff \  
&& \  
pip install --upgrade awscli==${AWSCLI_VERSION} awsebcli  
  
WORKDIR /data  
  
ENTRYPOINT ["aws"]

