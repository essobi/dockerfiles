FROM ubuntu:14.04  
MAINTAINER Ivan Foong <vonze21@gmail.com>  
  
ADD libraries/libswiftCore.so /usr/local/swift/lib/swift/linux/libswiftCore.so  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libicu52 \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD samples/hello /root/hello  
WORKDIR /root  
  
CMD ["bash"]  

