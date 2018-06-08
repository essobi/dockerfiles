FROM gliderlabs/alpine:3.6  
MAINTAINER Paulo Whyte <whyte@wisemonkey.com.br>  
  
ENV S3_TMP /tmp/s3cmd.zip  
ENV S3_ZIP /tmp/s3cmd-master  
  
WORKDIR /tmp  
  
RUN apk --no-cache add \  
unzip \  
coreutils \  
bash \  
curl \  
jq \  
py-pip \  
python &&\  
pip install --upgrade \  
pip \  
python-dateutil &&\  
curl -sSL --output ${S3_TMP}
https://github.com/s3tools/s3cmd/archive/master.zip &&\  
unzip -q ${S3_TMP} -d /tmp &&\  
mv ${S3_ZIP}/S3 ${S3_ZIP}/s3cmd /usr/bin/ &&\  
rm -rf /tmp/* &&\  
mkdir ~/.aws  
  
WORKDIR ~  
  
COPY ./get-objects /usr/local/bin/  
  
# Expose volume for adding credentials  
# VOLUME ["~/.aws"]  
ENTRYPOINT ["/bin/bash"]  

