  
FROM openjdk:jre-alpine  
MAINTAINER Frederic LOUI <frederic.loui@@renater.fr>  
  
RUN mkdir -p /opt/freertr && \  
mkdir -p /opt/freertr/bin && \  
mkdir -p /opt/freertr/src && \  
mkdir -p /opt/freertr/run  
  
WORKDIR /opt/freertr/  
  
RUN wget http://freerouter.nop.hu/rtr.zip http://freerouter.nop.hu/rtr.jar &&
\  
mv ./rtr.jar ./bin && \  
unzip ./rtr.zip -d /opt/freertr/src  
  
COPY . /opt/freertr/  
  
WORKDIR /opt/freertr/src  
RUN mkdir ./binTmp  
RUN apk update && apk upgrade && apk add --no-cache \  
gcc \  
musl-dev \  
libpcap-dev \  
linux-headers \  
openrc \  
ethtool  
WORKDIR /opt/freertr/src/misc/native/  
RUN ./c.sh  
WORKDIR /opt/freertr/  
RUN mv ./src/binTmp/* ./bin  
  
RUN apk del gcc musl-dev linux-headers  
  
VOLUME ./run:/opt/freertr/run  
  
ENV FREERTR_HOSTNAME=freertr \  
FREERTR_INTF_LIST="eth2/20010/20011"  
CMD ./scripts/freertr.sh -i $FREERTR_INTF_LIST -r $FREERTR_HOSTNAME  

