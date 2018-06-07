FROM gliderlabs/consul-server:0.6  
ADD ./config /config/  
EXPOSE 53 53/udp  
RUN apk update && \  
apk add bind  
COPY ./named.conf /etc/bind/named.conf  
COPY start.sh /usr/local/bin/container-start  
ENTRYPOINT ["container-start", "/bin/consul", "agent", "-server", "-config-
dir=/config"]

