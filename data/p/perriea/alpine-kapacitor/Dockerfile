FROM alpine:3.7  
LABEL MAINTAINER="Aurelien PERRIER <a.perrier89@gmail.com>"  
LABEL APP="kapacitor"  
LABEL APP_VERSION="1.4.0"  
LABEL APP_REPOSITORY="https://github.com/influxdata/kapacitor/releases"  
  
ENV TIMEZONE Europe/Paris  
ENV KAPACITOR_VERSION 1.4.0  
# Installing packages  
RUN apk add --no-cache su-exec  
  
# Work path  
WORKDIR /scripts  
  
# Downloading binaries  
ADD
https://dl.influxdata.com/kapacitor/releases/kapacitor-${KAPACITOR_VERSION}-static_linux_amd64.tar.gz
./  
RUN addgroup kapacitor && \  
adduser -s /bin/false -G kapacitor -S -D kapacitor  
  
# Coping scripts  
COPY scripts/start.sh start.sh  
  
# Extract archive  
RUN tar -C ./ -xzf kapacitor-${KAPACITOR_VERSION}-static_linux_amd64.tar.gz &&
\  
rm -f kapacitor-*/kapacitor.conf && \  
chmod +x kapacitor-*/* && \  
cp -a kapacitor-*/* /usr/bin/ && \  
rm -rf *.tar.gz* kapacitor-*  
  
VOLUME [ "/var/lib/kapacitor" ]  
  
EXPOSE 9092  
ENTRYPOINT ["./start.sh"]

