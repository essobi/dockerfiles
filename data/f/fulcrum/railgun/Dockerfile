# https://www.cloudflare.com/docs/railgun/installation.html  
  
FROM ubuntu:xenial  
RUN apt-get update && \  
apt-get install -y curl && \  
echo 'deb http://pkg.cloudflare.com/ xenial main' | tee
/etc/apt/sources.list.d/cloudflare-main.list && \  
curl -C - https://pkg.cloudflare.com/pubkey.gpg | apt-key add - && \  
apt-get update && \  
apt-get install -y railgun-stable  
WORKDIR /  
CMD [ "rg-listener", "-config=/etc/railgun/railgun.conf" ]  
  
  
# so rsyslog just would not work  
#FROM centos:7  
#RUN rpm -ivh http://pkg.cloudflare.com/cloudflare-release-latest.el7.rpm && \  
# yum update --security && \  
# yum install -y railgun-stable ca-certificates rsyslog && \  
# rm -rf /var/cache/yum /var/log/yum.log && \  
# cd / && ln -s /etc/railgun && \  
# cd /etc/railgun && find /etc/railgun -type f -exec cp {} {}-default \;  
#COPY entrypoint.sh /entrypoint.sh  
#COPY rsyslog.conf /etc/rsyslog.conf  
#WORKDIR /  
#EXPOSE 2408  
#ENTRYPOINT [ "/entrypoint.sh" ]  
#CMD [ "-config=/etc/railgun/railgun.conf" ]  

