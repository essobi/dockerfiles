FROM openjdk:8-jre-alpine  
ENV SOAPUI_VERSION 5.3.0  
RUN apk add --update python nodejs bash gcc make g++ curl && \  
npm install -g node-red node-red-node-base64 && \  
mkdir -p /home/nodered/.node-red/ /opt && \  
curl
http://cdn01.downloads.smartbear.com/soapui/${SOAPUI_VERSION}/SoapUI-${SOAPUI_VERSION}-linux-
bin.tar.gz \  
| gunzip -c - | tar -xf - -C /opt && \  
ln -s /opt/SoapUI-${SOAPUI_VERSION} /opt/SoapUI && \  
apk del gcc make g++ && \  
rm -Rf /var/cache/apk/* /tmp/* && npm cache clean  
ENV PATH ${PATH}:/opt/SoapUI/bin  
COPY ./static-settings.js /root/.node-red/settings.js  
COPY ./flows.json /home/nodered/.node-red/flows.json  
COPY ./process.py /home/nodered/process.py  
RUN chmod 700 /home/nodered/process.py  
ENTRYPOINT ["/usr/bin/node-red", "-v"]  

