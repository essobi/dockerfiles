FROM grahamgilbert/git-fat  
ADD 06-s3_sync.sh /docker-entrypoint.d/06-s3_sync.sh  
RUN apt-get update && \  
apt-get install -y python-pip python-dev build-essential git && \  
pip install awscli && \  
chmod 755 /docker-entrypoint.d/06-s3_sync.sh \  
&& rm -rf /var/lib/apt/lists/*  

