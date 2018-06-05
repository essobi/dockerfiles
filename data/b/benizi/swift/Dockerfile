# ubuntu:15.10 at some point in time:  
FROM
ubuntu@sha256:ae24faeb7d968197008eb7fa6970d1aa90636963947fe3486af27b079cccfb17  
  
RUN apt-get update && apt-get install -y \  
curl clang libicu-dev libedit-dev python2.7-dev  
  
ADD checksum /  
RUN curl -so /targz
https://swift.org/builds/ubuntu1510/swift-2.2-SNAPSHOT-2015-12-01-b/swift-2.2-SNAPSHOT-2015-12-01-b-ubuntu15.10.tar.gz
&& \  
sha256sum -c /checksum && \  
mkdir /swift && \  
tar --strip-components=2 -C /swift -xz < /targz && \  
rm /targz  
  
WORKDIR /src  
ENV PATH="/swift/bin:$PATH"  
CMD bash  
  
ADD stringtest.swift /  
ADD test /  

