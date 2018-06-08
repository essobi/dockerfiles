FROM alpine:3.3  
  
ADD latest_auth_plug.sh /tmp/  
ADD conf/mosquitto.conf /tmp/mosquitto.test.conf  
RUN apk --update upgrade \  
&& apk add mosquitto \  
&& /tmp/latest_auth_plug.sh \  
&& rm /tmp/latest_auth_plug.sh \  
&& rm -rf /var/cache/apk/*  
  

