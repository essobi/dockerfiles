ARG BASE=alpine  
FROM ${BASE}  
  
ENV TINI_VERSION v0.17.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-
static-amd64 /tini  
  
RUN apk add --no-cache openvpn curl bind-tools nmap-ncat parallel openresolv
python coreutils bash && \  
mkdir /vpn-testbot && chmod +x /tini  
  
ENV SPEEDTEST_SERVER_PORT 8000  
ADD src/testbot.sh /vpn-testbot/testbot.sh  
  
ENTRYPOINT ["/tini", "-g", "--", "/vpn-testbot/testbot.sh"]  

