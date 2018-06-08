FROM ubuntu:xenial  
MAINTAINER bender.rodriges <bender.rodriges@gmail.com>  
  
EXPOSE 22133  
RUN apt-get update \  
&& apt-get -y install curl  
  
RUN mkdir /siberite-data  
  
RUN curl -L -O
https://github.com/bogdanovich/siberite/releases/download/v0.6.2/siberite-0.6.2-linux_x86_64.tgz
\  
&& tar -xf siberite-0.6.2-linux_x86_64.tgz \  
&& rm -rf siberite-0.6.2-linux_x86_64.tgzz  
  
VOLUME /siberite-data  
  
WORKDIR siberite-0.6.2-linux_x86_64  
  
CMD ["./siberite", "-listen", "localhost:22133", "-data", "/siberite-data"]  

