FROM alpine  
MAINTAINER Emmanuel Rosa <emmanuel_rosa@aol.com>  
  
# download kindlegen and install it to /usr/bin  
RUN wget
http://kindlegen.s3.amazonaws.com/kindlegen_linux_2.6_i386_v2_9.tar.gz -O - |
tar -xzf - -C /usr/bin kindlegen  
  
RUN mkdir -p /source  
WORKDIR /source  

