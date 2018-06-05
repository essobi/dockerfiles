FROM golang:1.8.3-alpine  
  
MAINTAINER Thomas Cheng <thomas@beamstyle.com.hk>  
  
##### References #####  
# https://github.com/serioja90/docker-goofys  
# https://github.com/arvindr226/alpine-ssh/blob/master/Dockerfile  
# sudo docker exec -it xxxxxxxxxx $(docker run -i -d alpine sh) sh  
##### SSH #####  
# Install SSH required packages  
RUN apk --update add --no-cache openssh bash \  
&& sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config \  
&& rm -rf /var/cache/apk/*  
  
EXPOSE 22  
##### Goofys #####  
# Install Goofys required packages  
RUN apk update && apk add gcc ca-certificates openssl musl-dev git fuse  
  
# Goofys  
RUN go get github.com/kahing/goofys  
RUN go install github.com/kahing/goofys  
  
# add syslog-ng (syslog required by Goofys)  
RUN apk add syslog-ng  
RUN echo "@version: 3.7" > /etc/syslog-ng/syslog-ng.conf  
RUN echo "source s_local {internal();network(transport("udp"));unix-
dgram("/dev/log");};" >> /etc/syslog-ng/syslog-ng.conf  
RUN echo "destination d_local {file("/var/log/messages");};" >> /etc/syslog-
ng/syslog-ng.conf  
RUN echo "log {source(s_local);destination(d_local);};" >> /etc/syslog-
ng/syslog-ng.conf  
  
ENV AWS_REGION ap-southeast-1  
ENV AWS_BUCKET_AND_PREFIX my-bucket:optional-prefix  
ENV AWS_ACCESS_KEY xxxxxxxxxx  
ENV AWS_SECRET_KEY xxxxxxxxxx  
  
ENV SSH_ROOT_PASSWORD=password  
ENV SSH_ADMIN_USERNAME=admin  
ENV SSH_ADMIN_PASSWORD=password  
ENV SSH_STARTUP_DIRECTORY=/mnt/s3  
  
ENV GOOFYS_MOUNT_DIR /mnt/s3  
ENV GOOFYS_STAT_CACHE_TTL 1m0s  
ENV GOOFYS_TYPE_CACHE_TTL 1m0s  
ENV GOOFYS_DIR_MODE 0770  
ENV GOOFYS_FILE_MODE 0770  
ADD ./run.sh /root/run.sh  
  
ENTRYPOINT ["sh"]  
CMD ["/root/run.sh"]  

