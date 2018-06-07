FROM jayroh/base:2.3.3-0.7.9  
# Install python dependencies  
RUN set -ex && \  
apk add --update \  
python \  
python-dev \  
py-pip \  
&& rm -rf /var/cache/apk/*  
  
# Install pip stuff  
RUN pip install --upgrade pip && \  
pip install python-dateutil  
  
# Install s3cmd  
RUN curl -o /tmp/s3cmd.tar.gz
http://assets.shubox.io.s3.amazonaws.com/s3cmd-1.5.2.tar.gz && \  
tar -xzf /tmp/s3cmd.tar.gz -C /tmp/ && \  
mv /tmp/s3cmd-1.5.2/s3cmd /usr/bin/ && \  
mv /tmp/s3cmd-1.5.2/S3 /usr/bin/ && \  
rm -rf /tmp/s3cmd*  
  
CMD ["./bin/docker-puma-run.sh"]  

