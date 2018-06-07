FROM busybox:glibc  
MAINTAINER it-operations@boerse-go.de  
ENV TOOL=vault \  
VERSION=0.5.2 \  
SHA256=7517b21d2c709e661914fbae1f6bf3622d9347b0fe9fc3334d78a01d1e1b4ec2  
  
# By using ADD there is no need to install wget or curl  
ADD
https://releases.hashicorp.com/${TOOL}/${VERSION}/${TOOL}_${VERSION}_linux_amd64.zip
${TOOL}_${VERSION}_linux_amd64.zip  
RUN echo "${SHA256} ${TOOL}_${VERSION}_linux_amd64.zip" | sha256sum -cw &&\  
unzip ${TOOL}_${VERSION}_linux_amd64.zip &&\  
rm -r ${TOOL}_${VERSION}_linux_amd64.zip  
  
ENTRYPOINT ["/vault"]  
CMD ["--help"]  

