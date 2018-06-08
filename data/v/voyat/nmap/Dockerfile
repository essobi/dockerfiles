FROM alpine:latest  
  
MAINTAINER Thierry VOYAT <thierry.voyat@ac-amiens.fr>  
  
RUN apk update \  
&& apk add tzdata && cp /usr/share/zoneinfo/Europe/Paris /etc/localtime \  
&& echo "Europe/Paris" > /etc/timezone \  
&& apk del tzdata \  
&& apk add \  
ca-certificates \  
openssl \  
nmap \  
nmap-ncat \  
nmap-nping \  
nmap-nselibs \  
nmap-scripts \  
&& update-ca-certificates \  
&& rm -rf /var/cache/apk/*  
  
# Les scripts nmap à inclure  
COPY FILES/. /usr/share/nmap/scripts/  
  
ENTRYPOINT ["/usr/bin/nmap"]  
CMD ["--help"]  

