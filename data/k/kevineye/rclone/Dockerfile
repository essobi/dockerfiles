FROM alpine:latest  
ARG RCLONE_VERSION="1.41"  
ADD
https://downloads.rclone.org/v${RCLONE_VERSION}/rclone-v${RCLONE_VERSION}-linux-
amd64.zip /  
RUN unzip rclone-*.zip  
  
FROM alpine:latest  
RUN apk --no-cache add ca-certificates  
COPY \--from=0 /rclone-*/rclone /usr/bin  
ENTRYPOINT ["rclone"]  
CMD ["--version"]  

