FROM alpine:latest  
  
MAINTAINER Kristian Østergaard Martensen <km@shipbeat.com>  
  
ENV TEAMCITY_BASE_URL https://teamcity.server.at.shipbeat \  
TEAMCITY_USERNAME teamcity \  
TEAMCITY_PASSWORD secret \  
AWS_S3_BUCKET teamcity-backup-bucket-at-shipbeat \  
AWS_ACCESS_KEY xxxxxxxx \  
AWS_SECRET_KEY xxxxxxxx \  
KEEP_DAYS 0  
RUN apk add --no-cache python3 && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
pip3 install argparse requests boto3 && \  
rm -r /root/.cache  
  
VOLUME ["/var/lib/teamcity"]  
  
COPY launch.sh /launch.sh  
COPY teamcity_backup.py /teamcity_backup.py  
COPY push_to_s3.py /push_to_s3.py  
  
RUN chmod +x /launch.sh  
  
ENTRYPOINT /launch.sh  

