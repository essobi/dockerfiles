FROM alpine  
  
ENV RCLONE_VERSION=1.40  
RUN apk add --no-cache wget unzip ca-certificates curl bash coreutils  
  
RUN wget
http://downloads.rclone.org/v${RCLONE_VERSION}/rclone-v${RCLONE_VERSION}-linux-
amd64.zip && \  
unzip rclone-v${RCLONE_VERSION}-linux-amd64.zip && \  
rm rclone-v${RCLONE_VERSION}-linux-amd64.zip && \  
mv rclone-*/rclone /usr/bin && \  
rm -rf rclone-*  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  
CMD [ "--help" ]  

