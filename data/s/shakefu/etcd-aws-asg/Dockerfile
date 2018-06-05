# Build image  
FROM alpine AS build  
  
ENV ETCD_VERSION 3.2.5  
WORKDIR /root  
  
# Install depdencies needed to build  
RUN apk --no-cache add \  
python \  
py-pip \  
curl  
  
# Create a /root/bin directory for our stuffs  
RUN mkdir ./bin  
  
# Download and install AWS CLI tools  
RUN pip install --upgrade awscli  
  
# Download and install etcd  
RUN curl -L
https://github.com/coreos/etcd/releases/download/v${ETCD_VERSION}/etcd-v${ETCD_VERSION}-linux-
amd64.tar.gz -o etcd.tar.gz && \  
tar xzf etcd.tar.gz && \  
mv etcd-*/etcd etcd-*/etcdctl ./bin  
  
# Run image  
FROM alpine  
  
# Install depdencies needed to run  
RUN apk --no-cache add \  
python \  
curl \  
bash \  
jq  
  
# Copy artifacts  
# etcd binaries  
COPY \--from=build /root/bin/* /usr/local/bin/  
# AWS CLI python libraries  
COPY \--from=build /usr/lib/python2.7/site-packages /usr/lib/python2.7  
# AWS CLI script  
COPY \--from=build /usr/bin/aws /usr/local/bin/aws  
# The run script  
COPY etcd-aws-asg /usr/local/bin/etcd-aws-asg  
  
# Our run command  
ENTRYPOINT ["/usr/local/bin/etcd-aws-asg"]  
  

