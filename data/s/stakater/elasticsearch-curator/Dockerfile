FROM stakater/python:2.7-alpine  
  
ARG CURATOR_VERSION=5.5.4  
  
ENV CRON_SCHEDULE="0 0 * * *" \  
ELASTICSEARCH_HOST="elasticsearch" \  
ELASTICSEARCH_PORT="9092" \  
SNAPSHOT_NAME="s3-backup" \  
BUCKET_NAME="es-backup-bucket" \  
BUCKET_BASE_PATH="/" \  
AWS_REGION="us-west-1" \  
TIME_UNIT="days" \  
TIMESTRING="%Y.%m.%d" \  
OLDER_THAN="90" \  
DO_SNAPSHOT="true" \  
DO_DELETE="true" \  
LOGLEVEL="INFO" \  
LOGFILE="/var/log/curator.log"  
RUN \  
pip install --no-cache-dir \  
elasticsearch-curator==${CURATOR_VERSION} \  
&& \  
mkdir /curator-config  
  
ADD ./curator-config /curator-config  
ADD start.sh /  
  
ENTRYPOINT [ ]  
CMD ["/start.sh"]

