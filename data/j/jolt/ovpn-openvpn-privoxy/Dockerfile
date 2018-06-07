FROM alpine:latest  
MAINTAINER Fredrik Lundhag <f@mekk.com>  
  
EXPOSE 8118  
RUN apk --update --no-cache add privoxy openvpn runit curl  
  
COPY app /app  
  
RUN cd /tmp && \  
curl -sLO https://files.ovpn.com/ubuntu_cli/ovpn-se.zip && \  
unzip ovpn-se.zip && mv config/* /etc/openvpn && \  
rm -rf config && rm ovpn-se.zip && rm /etc/openvpn/ovpn.conf  
  
RUN find /app -name run | xargs chmod u+x && \  
chmod 0400 /etc/openvpn/ovpn-tls.key  
  
# Comment out stuff we don't need from the ovpn-provided configs  
RUN sed -i 's/^\\(up\\)/#\1/; s/^\\(down\\)/#\1/; s/^\\(log\\)/#\1/'
app/openvpn/config/*.conf  
  
ENV REGION="se" \  
USERNAME="" \  
PASSWORD="" \  
LOCAL_NETWORK=172.16.0.0/12  
CMD ["runsvdir", "/app"]  

