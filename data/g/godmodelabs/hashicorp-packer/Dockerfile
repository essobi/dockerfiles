FROM busybox:glibc  
MAINTAINER it-operations@boerse-go.de  
ENV TOOL=packer \  
VERSION=0.9.0 \  
SHA256=4119d711855e8b85edb37f2299311f08c215fca884d3e941433f85081387e17c  
  
ADD
https://releases.hashicorp.com/${TOOL}/${VERSION}/${TOOL}_${VERSION}_linux_amd64.zip
${TOOL}_${VERSION}_linux_amd64.zip  
RUN echo "${SHA256} ${TOOL}_${VERSION}_linux_amd64.zip" | sha256sum -cw &&\  
unzip ${TOOL}_${VERSION}_linux_amd64.zip &&\  
rm -r ${TOOL}_${VERSION}_linux_amd64.zip  
  
ENTRYPOINT ["/packer"]  
CMD ["--help"]  

