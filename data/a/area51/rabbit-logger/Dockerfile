FROM alpine:latest  
  
RUN wget -O /etc/apk/keys/jenkins-5782b282.rsa.pub
http://packages.area51.onl/alpine/jenkins-5782b282.rsa.pub &&\  
echo http://packages.area51.onl/alpine >>/etc/apk/repositories &&\  
apk add --update rabbit-logger &&\  
rm -rf /var/lib/apt/lists/*  

