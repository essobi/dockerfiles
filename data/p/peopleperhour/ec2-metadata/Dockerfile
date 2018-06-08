FROM gliderlabs/alpine:3.1  
MAINTAINER Panagiotis Moustafellos <pmoust@peopleperhour.com>  
RUN apk-install curl bash && \  
curl -O -k --silent https://s3.amazonaws.com/ec2metadata/ec2-metadata && \  
chmod +x /ec2-metadata  
ENTRYPOINT ["/ec2-metadata"]  

