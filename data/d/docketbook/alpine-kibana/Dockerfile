FROM mhart/alpine-node:5.11  
MAINTAINER Dave Finster <df@docketbook.io>  
  
RUN apk update && \  
apk add bash openssl && \  
cd ~ && \  
wget https://download.elastic.co/kibana/kibana/kibana-4.5.0-linux-x64.tar.gz
&& \  
tar -zxvf kibana-4.5.0-linux-x64.tar.gz && \  
rm kibana-4.5.0-linux-x64.tar.gz && \  
mv kibana-4.5.0-linux-x64 /kibana && \  
rm -rf /kibana/node  
  
ADD configurations /kibana/config  
  
EXPOSE 5601  
ENTRYPOINT [ "/kibana/bin/kibana"]

