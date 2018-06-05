FROM debian  
MAINTAINER John Goodall <jgoodall@ornl.gov>  
  
LABEL program=argus  
  
ENV PROG argus  
ENV VERS 3.0.8.2  
ENV PREFIX /opt  
ENV PATH
$PREFIX/sbin:$PREFIX/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
RUN apt-get update -qq && \  
apt-get install -yq curl gcc make bison flex libpcap-dev libwrap0-dev patch
--no-install-recommends  
  
COPY argus.patch /tmp/argus.patch  
  
WORKDIR /tmp  
RUN curl -sL http://qosient.com/argus/src/$PROG-$VERS.tar.gz | tar -zxf - && \  
cd $PROG-$VERS && \  
patch -p0 < /tmp/argus.patch && \  
./configure --prefix=$PREFIX && \  
make && \  
make install && \  
rm -rf /tmp/$PROG-$VERS /tmp/argus.patch  
  
WORKDIR $PREFIX  
ENTRYPOINT ["/opt/sbin/argus"]  
CMD ["-h"]  
  

