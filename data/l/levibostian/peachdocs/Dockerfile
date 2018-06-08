FROM golang:1.9.1-alpine3.6  
MAINTAINER Levi Bostian levi.bostian@gmail.com  
  
RUN apk -U --no-progress upgrade \  
&& apk -U --no-progress add wget git  
  
RUN cd /root  
RUN wget
https://github.com/peachdocs/peach/releases/download/v0.9.2/linux_amd64.zip  
RUN unzip linux_amd64.zip  
RUN mv peach /usr/bin/  
RUN chmod +x /usr/bin/peach  
  
RUN mkdir /site.peach  
WORKDIR /site.peach  
  
EXPOSE 5555  
CMD peach web  

