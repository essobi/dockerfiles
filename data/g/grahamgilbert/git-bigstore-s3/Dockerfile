FROM grahamgilbert/git-bigstore  
ADD 05-s3_sync.sh /docker-entrypoint.d/05-s3_sync.sh  
RUN pip install awscli && chmod 755 /docker-entrypoint.d/05-s3_sync.sh  

