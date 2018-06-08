FROM alpine:3.2  
MAINTAINER Jonathon W. Marshall "jonathon@gallop.io"  
RUN apk --update add ca-certificates bash tar && rm -rf /var/cache/apk/*  
  
ADD
https://github.com/bitly/oauth2_proxy/releases/download/v2.0.1/oauth2_proxy-2.0.1.linux-
amd64.go1.4.2.tar.gz /tmp/oauth2_proxy.tar.gz  
RUN mkdir -p /srv && tar -xzvf /tmp/oauth2_proxy.tar.gz -C /srv/  
RUN ln -s /srv/oauth2_proxy-2.0.1.linux-amd64.go1.4.2/oauth2_proxy
/usr/local/bin/oauth2_proxy  
RUN rm -f /tmp/oauth2_proxy.tar.gz  
  
#RUN apt-get update && apt-get install -y wget  
#RUN wget -q
https://github.com/bitly/oauth2_proxy/releases/download/v2.0.1/oauth2_proxy-2.0.1.linux-
amd64.go1.4.2.tar.gz  
#RUN tar -xzvf /oauth2_proxy-2.0.1.linux-amd64.go1.4.2.tar.gz -C /srv/  
#RUN ln -s /srv/oauth2_proxy-2.0.1.linux-amd64.go1.4.2/oauth2_proxy
/usr/local/bin/oauth2_proxy  
#RUN rm /oauth2_proxy-2.0.1.linux-amd64.go1.4.2.tar.gz  
COPY run.sh /run.sh  
  
EXPOSE 443  
EXPOSE 4180  
ENTRYPOINT ["/run.sh"]  

