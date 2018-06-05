FROM golang:1.9-stretch  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update -y && apt-get upgrade -y && \  
apt-get -y install git && apt-get -y autoclean  
  
WORKDIR /go/src/oncall-buddy-finder  
COPY src/ .  
COPY etc/ /etc/oncall-buddy-finder/  
  
RUN go-wrapper download  
RUN go-wrapper install  
RUN mkdir /var/run/oncall-buddy-finder && chmod 755 /var/run/oncall-buddy-
finder  
  
CMD ["go-wrapper", "run"]  
  
ENV CONFIG=/etc/oncall-buddy-finder/config-docker.json  
  
VOLUME /etc/oncall-buddy-finder  
VOLUME /var/run/oncall-buddy-finder  

