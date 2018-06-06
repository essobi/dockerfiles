FROM golang:stretch  
  
ENV RELEASE="certstrap.tar.gz"  
COPY $RELEASE /tmp/$RELEASE  
  
RUN cd /tmp && \  
tar -xzf $RELEASE && \  
cd certstrap && \  
./build  
  
FROM ryanjohnston/base:latest  
  
LABEL vendor=Bespoke\ View\ Consulting\ Incorporated \  
com.bespokeview.version="0.0.1" \  
com.bespokeview.name="ryanjohnston/certstrap"  
  
VOLUME /workdir/  
  
WORKDIR /workdir/  
  
COPY \--from=0 /tmp/certstrap/bin/certstrap-v1.1.1-linux-amd64 /bin/certstrap  
  
ENTRYPOINT [ "/bin/certstrap" ]  

