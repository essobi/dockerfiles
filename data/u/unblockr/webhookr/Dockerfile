FROM golang:1.5  
MAINTAINER Mark Howells  
  
# Set noninteractive mode for apt-get...  
ENV DEBIAN_FRONTEND noninteractive  
  
# set etcd endpoint defaulkt  
ENV ETCD_ENDPOINT=https://172.17.42.1:2379  
# Upgrade base system packages  
RUN apt-get update  
  
# Now add ssh stuff and sudo  
RUN apt-get install -y ssh sudo \  
&& apt-get install -y wget  
  
### Replace the SSH key with a new one #####  
RUN rm -rf /root/.ssh/id_rsa  
  
# Generate SSH deployment key (could be overwrite by a volume)  
RUN ssh-keygen -N "" -f /root/.ssh/id_rsa  
  
# grab the webhook app  
RUN go get github.com/adnanh/webhook  
  
### Replace scripts with our scripts (may still be overwritten)  
ADD ./scripts /var/opt/webhookr/scripts  
COPY ./hooks.json /var/opt/webhookr/  
RUN chmod a+x -R /var/opt/webhookr/scripts  
  
# Ignore strict host key checking  
RUN echo "Host github.com\n\tStrictHostKeyChecking no\n" >> /root/.ssh/config
&& \  
echo "Host bitbucket.org\n\tStrictHostKeyChecking no\n" >> /root/.ssh/config  
  
# Now install etcdctl  
RUN wget
https://github.com/coreos/etcd/releases/download/v2.2.0/etcd-v2.2.0-linux-
amd64.tar.gz -O etcd-v2.2.0-linux-amd64.tar.gz  
RUN tar xzvf etcd-v2.2.0-linux-amd64.tar.gz  
RUN cp etcd-v2.2.0-linux-amd64/etcdctl /bin/  
  
# Change workdir  
WORKDIR /var/opt/webhookr  
  
# Port  
EXPOSE 9000  
CMD []  
ENTRYPOINT ["/go/bin/webhook", "-hooks", "hooks.json","--verbose"]  

