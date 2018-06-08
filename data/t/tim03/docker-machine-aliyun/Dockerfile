FROM tim03/go  
LABEL maintainer Chen, Wenli <chenwenli@chenwenli.com>  
  
ENV ECS_ACCESS_KEY_ID ''  
ENV ECS_ACCESS_KEY_SECRET ''  
ENV ECS_API_ENDPOINT ''  
ENV ECS_DESCRIPTION ''  
ENV ECS_DISK_SIZE 0  
ENV ECS_DISK_CATEGORY 'cloud'  
ENV ECS_SYSTEM_DISK_SIZE 40  
ENV ECS_SYSTEM_DISK_CATEGORY 'cloud'  
ENV ECS_IMAGE_ID ''  
ENV ECS_IO_OPTIMIZED 'none'  
ENV ECS_INSTANCE_TYPE 'ecs.t1.small'  
ENV ECS_INTERNET_MAX_BANDWIDTH 100  
ENV ECS_PRIVATE_ADDR_ONLY false  
ENV ECS_REGION 'cn-shanghai'  
ENV ECS_ROUTE_CIDR ''  
ENV ECS_SECURITY_GROUP 'default'  
ENV ECS_SLB_ID ''  
ENV ECS_SSH_PASSWORD ''  
ENV ECS_TAGS 'auto'  
ENV ECS_VPC_ID ''  
ENV ECS_VSWITCH_ID ''  
ENV ECS_ZONE ''  
RUN \  
curl -L https://github.com/docker/machine/releases/download/v0.12.0/docker-
machine-`uname -s`-`uname -m` >/tmp/docker-machine && \  
chmod +x /tmp/docker-machine && \  
cp /tmp/docker-machine /usr/local/bin/docker-machine && \  
mkdir -p /root/.docker/machine  
  
RUN \  
cd $GOPATH && \  
go get -d github.com/AliyunContainerService/docker-machine-driver-aliyunecs &&
\  
go install github.com/AliyunContainerService/docker-machine-driver-aliyunecs  
  
COPY ./entry_point.sh /  
  
ENTRYPOINT ["/entry_point.sh"]  
CMD ["--help"]  

