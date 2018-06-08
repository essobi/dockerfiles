FROM alpine:3.6  
LABEL maintainer="Yorick Poels <yorick.poels@gmail.com>"  
  
ENV VERSION=1.6.2  
RUN apk add --no-cache wget tar bash perl &&\  
rm -rf /var/cache/apk/*  
  
WORKDIR /tmp  
  
RUN wget https://github.com/rfxn/linux-malware-
detect/archive/"$VERSION".tar.gz --no-check-certificate &&\  
tar -xvf "$VERSION".tar.gz  
  
WORKDIR /tmp/linux-malware-detect-"$VERSION"  
RUN bash -x install.sh  
  
COPY ./files/internals/internals.conf
/usr/local/maldetect/internals/internals.conf  
  
RUN /usr/local/maldetect/maldet -u  
  
ENTRYPOINT ["/usr/local/maldetect/maldet"]  

