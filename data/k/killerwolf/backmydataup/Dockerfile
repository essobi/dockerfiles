FROM alpine:latest  
  
MAINTAINER killerwolf <killerwolf06@gmail.com> @killerwolf  
  
#dedicated backup volume  
VOLUME /backup  
  
# Install awscli  
WORKDIR /tmp  
RUN apk add --update python groff \  
&& wget http://s3.amazonaws.com/aws-cli/awscli-bundle.zip -O awscli-bundle.zip
\  
&& unzip awscli-bundle.zip \  
&& ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws \  
&& rm awscli-bundle.zip \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf awscli-bundle  
  
#Configure AWS cli  
ENV AWS_ACCESS_KEY_ID AWS_ACCESS_KEY_ID  
ENV AWS_SECRET_ACCESS_KEY AWS_SECRET_ACCESS_KEY  
ENV S3_BUCKET S3_BUCKET  
  
# create archive of volume folder and store it on AWS  
ADD backmydataup.sh /backmydataup.sh  
RUN chmod +x /backmydataup.sh  
CMD ["/backmydataup.sh"]  

