FROM alpine:latest  
MAINTAINER Firespring "info.dev@firespring.com"  
RUN apk add --update gettext curl python unzip && \  
rm -rf /var/cache/apk/*  
  
# install latest awscli and clean up  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip" \  
&& unzip awscli-bundle.zip \  
&& ./awscli-bundle/install -i /usr/local/ \  
&& rm -rf awscli-bundle/* awscli-bundle.zip  
  
ENV AWS_DEFAULT_REGION=us-west-2 \  
AWS_ACCESS_KEY_ID='' \  
AWS_SECRET_ACCESS_KEY='' \  
AWS_SESSION_TOKEN='' \  
AWS_OPTIONS='' \  
AWS_SYNC_OPTIONS='' \  
SOURCE_LOCATION='/directory' \  
DEST_LOCATION='s3://bucket' \  
SYNC_PERIOD=0  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["aws $AWS_OPTIONS s3 sync $AWS_SYNC_OPTIONS $SOURCE_LOCATION
$DEST_LOCATION"]  

