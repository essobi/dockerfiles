FROM minio/minio  
  
RUN apk add --no-cache bash git curl openjdk8  
RUN \  
curl -sL "https://github.com/sbt/sbt/releases/download/v1.0.4/sbt-1.0.4.tgz" |
tar -xzf - -C /usr/local && \  
ln -s /usr/local/sbt/bin/sbt /usr/local/bin/sbt && \  
chmod 0755 /usr/local/bin/sbt && \  
sbt exit  
  
# Credentials used by the unit tests  
ENV MINIO_ACCESS_KEY J0148KUQZZMATIGD1C1N  
ENV MINIO_SECRET_KEY ZVRPanENsg4lLXehZpaM1bXcksItQ5MqiKBvVV4D  
  
WORKDIR /root  
  
# there will be the bitbucket-pipelines.yml scripts injected...  
ENTRYPOINT /bin/bash  

