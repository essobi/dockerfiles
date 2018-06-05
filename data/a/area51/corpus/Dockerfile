FROM alpine:latest  
MAINTAINER Peter Mount <peter@retep.org>  
  
# Port to serve api on  
ENV PORT 4000  
# Age in days on restart to download new file  
ENV MAXAGE 1  
VOLUME /opt/data  
  
COPY *.sh /  
  
CMD ["/docker-entrypoint.sh"]  
  
#RUN apk add --update curl &&\  
# curl -o /etc/apk/keys/jenkins-5782b282.rsa.pub
http://packages.area51.onl/alpine/jenkins-5782b282.rsa.pub &&\  
RUN wget -O /etc/apk/keys/jenkins-5782b282.rsa.pub
http://packages.area51.onl/alpine/jenkins-5782b282.rsa.pub &&\  
echo http://packages.area51.onl/alpine >>/etc/apk/repositories &&\  
apk add --update curl nrod-corpus &&\  
chmod +x /*.sh &&\  
rm -rf /var/cache/apk/*  

