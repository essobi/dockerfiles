FROM busybox:glibc  
MAINTAINER it-operations@boerse-go.de  
ENV TOOL=consul-template \  
VERSION=0.14.0 \  
SHA256=7c70ea5f230a70c809333e75fdcff2f6f1e838f29cfb872e1420a63cdf7f3a78  
  
# By using ADD there is no need to install wget or curl  
ADD
https://releases.hashicorp.com/${TOOL}/${VERSION}/${TOOL}_${VERSION}_linux_amd64.zip
${TOOL}_${VERSION}_linux_amd64.zip  
RUN echo "${SHA256} ${TOOL}_${VERSION}_linux_amd64.zip" | sha256sum -cw &&\  
unzip ${TOOL}_${VERSION}_linux_amd64.zip &&\  
rm -r ${TOOL}_${VERSION}_linux_amd64.zip  
  
ENTRYPOINT ["/consul-template"]  
CMD ["--help"]  

