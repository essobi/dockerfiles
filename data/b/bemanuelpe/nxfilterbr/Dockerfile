FROM alpine:3.4  
ENV NXF_VERSION 3.4.3  
ENV NXF_ZIP nxfilter-${NXF_VERSION}.zip  
  
RUN apk add --update git curl unzip openjdk8-jre && rm -rf /var/cache/apk/  
ADD http://nxfilter.org/download/${NXF_ZIP} /usr/local/  
RUN mkdir -p /nxfilter/skins && unzip /usr/local/${NXF_ZIP} -d /nxfilter && rm
/usr/local/${NXF_ZIP} && chmod +x /nxfilter/bin/*.sh  
  
WORKDIR /nxfilter/bin  
  
RUN /usr/bin/git clone https://github.com/bemanuel/nxfskinbr.git
/usr/local/nxfskinbr && mv /usr/local/nxfskinbr/skins/nxfskinbr
/nxfilter/skins/. && apk del git curl unzip && rm -rf /usr/local/nxfskinbr  
  
EXPOSE 53 80 443 514 2055 19001 19002 19003 19004 19005  
ENTRYPOINT ["/nxfilter/bin/startup.sh"]  

