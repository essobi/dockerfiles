FROM alpine:3.4  
MAINTAINER ashmastaflash  
  
RUN apk update && apk add \  
easy-rsa \  
python \  
py-pip  
  
RUN pip install hvac  
  
RUN mkdir -p /etc/sitch/crypto  
  
WORKDIR /usr/share/easy-rsa/  
  
COPY ./vars /usr/share/easy-rsa/  
COPY ./cryptogen.sh /usr/share/easy-rsa/  
COPY ./ /app  
  
CMD /usr/share/easy-rsa/cryptogen.sh  

