FROM alpine:3.4  
RUN apk --update add rsyslog bash wget  
RUN apk --update add --virtual builddeps build-base git go  
  
ENV BOSUN_VERSION 0.5.0  
ENV GOPATH /tmp/bosun  
  
RUN mkdir -p /opt/bosun/bin ${GOPATH}/src/  
WORKDIR /tmp/bosun/src  
RUN git clone -b ${BOSUN_VERSION} \--depth 1 https://github.com/bosun-
monitor/bosun.git bosun.org  
WORKDIR /tmp/bosun/src/bosun.org/cmd/bosun  
RUN go build  
RUN cp /tmp/bosun/src/bosun.org/cmd/bosun/bosun /opt/bosun/bin/  
  
RUN rm -rf ${GOPATH} && apk del builddeps && rm -rf /var/cache/apk/*  
  
RUN mkdir -p /opt/bin/ /etc/bosun  
ADD docker/start_bosun.sh /opt/bin/  
ADD docker/bosun.conf /etc/bosun/bosun.conf  
  
ENTRYPOINT ["/opt/bin/start_bosun.sh"]  
  
EXPOSE 8070  
VOLUME ["/etc/bosun", "/var/run/bosun"]  

