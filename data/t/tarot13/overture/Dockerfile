FROM alpine  
  
LABEL maintainer "Ian Li <OpenSource@ianli.xyz>"  
  
RUN apk add --no-cache curl git unzip && \  
cd /root && \  
curl -SL
"https://github.com/shawn1m/overture/releases/download/1.3.6/overture-linux-
amd64.zip" -o overture.zip && \  
mkdir -p overture && \  
unzip overture.zip -d ./overture/ && \  
mv overture/overture-linux-amd64 /usr/sbin/overture && \  
rm -rf ./overture/ && \  
rm overture.zip  
  
ENTRYPOINT ["/usr/sbin/overture"]  
  
CMD ["-c", "/etc/overture/config.json"]

