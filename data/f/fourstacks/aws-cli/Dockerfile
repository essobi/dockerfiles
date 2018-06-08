FROM alpine:3.4  
MAINTAINER Make.io <info@make.io>  
  
ENV S3_TMP /tmp/s3cmd.zip  
ENV S3_ZIP /tmp/s3cmd-master  
ENV PAGER more  
  
ENV AWS_CLI_VERSION 1.11.11  
ENV BOTO3_VERSION 1.4.1  
WORKDIR /tmp  
  
RUN apk add --update-cache \  
bash \  
bash-completion \  
groff \  
less \  
curl \  
jq \  
build-base \  
py-pip \  
python && \  
rm -rf /var/cache/apk/*  
  
RUN pip install --upgrade \  
awscli==${AWS_CLI_VERSION} \  
boto3==${BOTO3_VERSION} \  
pip \  
python-dateutil  
  
RUN ln -s /usr/bin/aws_bash_completer /etc/profile.d/aws_bash_completer.sh  
  
RUN curl -sSL --output ${S3_TMP}
https://github.com/s3tools/s3cmd/archive/master.zip &&\  
unzip -q ${S3_TMP} -d /tmp &&\  
mv ${S3_ZIP}/S3 ${S3_ZIP}/s3cmd /usr/bin/ && \  
rm -rf /tmp/* &&\  
mkdir ~/.aws &&\  
chmod 700 ~/.aws  
  
VOLUME ["~/.aws"]  
  
CMD ["/bin/bash", "--login"]  

