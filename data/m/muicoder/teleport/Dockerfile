FROM muicoder/glibc  
  
ENV TELEPORT=2.3.5 \  
NODENAME=dockertest \  
AUTH_TOKEN=41c0c66c55ef2dcc382f6358919ef3f2  
  
RUN apk add --no-cache make && \  
cd /tmp && \  
curl -sSL
https://github.com/gravitational/teleport/releases/download/v${TELEPORT}/teleport-v${TELEPORT}-linux-
amd64-bin.tar.gz \  
-o teleport-v${TELEPORT}-linux-amd64-bin.tar.gz && \  
tar xf teleport-v${TELEPORT}-linux-amd64-bin.tar.gz && \  
cd teleport && \  
make install && \  
curl -sSL https://github.com/muicoder/teleport/raw/master/teleport.yml \  
-o /etc/teleport.yml && \  
sed -i "s/nodename: graviton/nodename: ${NODENAME}/g" /etc/teleport.yml && \  
sed -i "s/auth_token: xxxx-token-xxxx/auth_token: ${AUTH_TOKEN}/g"
/etc/teleport.yml && \  
apk del make && \  
rm -rf /tmp/*  
  
VOLUME ["/var/lib/teleport"]  
  
EXPOSE 3022 3023 3024 3025 3080  
ENTRYPOINT ["teleport"]  
CMD ["start"]  

