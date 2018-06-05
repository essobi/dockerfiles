FROM stakater/aws-cli  
LABEL authors="Hazim <hazim_malik@hotmail.com>"  
  
ENV S3_BUCKET_LOCATION myBucket/myFolder  
ADD s3sync.sh /s3sync.sh  
RUN chmod a+x /s3sync.sh  
ADD start.sh /services/s3sync/run  
VOLUME ["/s3sync"]

