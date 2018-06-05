FROM alpine:3.4  
MAINTAINER Jesse B. Crawford <admin@jbcrawford.us>  
# Based on verb/znc from Lee Verberne <lee@blarg.org>  
RUN apk add --update \  
ca-certificates \  
g++ \  
git \  
make \  
openssl-dev \  
curl \  
sudo  
RUN curl http://znc.in/releases/znc-latest.tar.gz -o /root/znc.tgz \  
&& cd /root && tar -xzf znc.tgz && cd /root/znc-1.6.3/ \  
&& ./configure && make && make install  
RUN adduser -S znc  
  
ADD entry.sh /entry.sh  
CMD chmod +x /entry.sh  
  
EXPOSE 45454  
ENTRYPOINT ["/entry.sh"]  
CMD [""]  

