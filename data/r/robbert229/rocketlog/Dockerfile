FROM alpine  
MAINTAINER John Rowley <johnrowleyster@gmail.com>  
  
WORKDIR /root/  
  
RUN apk update && apk add openssl  
RUN wget
https://github.com/hamstak/rocketlog/releases/download/v0.0.3/rocketlog_0.0.3_linux_386.tar.gz
&& \  
tar -xzvf ./rocketlog_0.0.3_linux_386.tar.gz  
  
ENTRYPOINT ["./rocketlog_0.0.3_linux_386/rocketlog", "-config",
"/root/configuration.yml"]  

