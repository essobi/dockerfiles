FROM resin/armhf-alpine  
  
EXPOSE 8118  
RUN apk --no-cache --update add privoxy && \  
sed -i'' 's/127\\.0\\.0\\.1:8118/0\\.0\\.0\\.0:8118/' /etc/privoxy/config && \  
sed -i'' 's/#debug 1/debug 1/' /etc/privoxy/config && \  
sed -i'' 's/#debug 1024/debug 1024/' /etc/privoxy/config && \  
sed -i'' 's/#debug 4096/debug 4096/' /etc/privoxy/config && \  
sed -i'' 's/#debug 8192/debug 8192/' /etc/privoxy/config && \  
echo "forward-socks5 / tor:9050 ." >> /etc/privoxy/config  
  
RUN chown privoxy.privoxy /etc/privoxy/*  
  
ENTRYPOINT ["/usr/sbin/privoxy"]  
CMD ["--no-daemon", "--user", "privoxy", "/etc/privoxy/config"]  

