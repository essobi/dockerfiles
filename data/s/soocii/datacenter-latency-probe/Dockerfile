FROM jonascheng/amazonlinux  
  
ENV S3_BUCKET_NAME=bucket  
#ENV S3_HOSTNAME=bucket.s3-ap-northeast-1.amazonaws.com  
ENV AWS_ACCESS_KEY_ID=access_key_id  
ENV AWS_SECRET_ACCESS_KEY=secret_access_key  
ENV AWS_DEFAULT_REGION=ap-southeast-1  
# add testing hugh file  
ADD test.mp4 /root  
  
# add testing script  
ADD entry.sh /root  
  
WORKDIR /root  
  
CMD ["/bin/sh", "-c", "/root/entry.sh > /var/log/probe.out 2>&1"]  

