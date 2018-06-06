FROM coolersport/alpine-java:8u162b12_server-jre_unlimited  
  
COPY run.sh /  
  
RUN apk add \--no-cache openssl git bash && \  
git clone https://github.com/floragunncom/search-guard-ssl.git /tmp/search-
guard-ssl && \  
mv /tmp/search-guard-ssl/example-pki-scripts/ /pki-scripts && \  
chmod +x /pki-scripts/*.sh && \  
sed -i 's/changeit/$CA_PASS/g' /pki-scripts/example.sh && \  
sed -i "s/-ext
san=dns:\$NODE_NAME.example.com,dns:localhost,ip:127.0.0.1,oid:1.2.3.4.5.5/-ext
san=\${SAN:+\${SAN},}dns:\$NODE_NAME.example.com,dns:localhost,ip:127.0.0.1,oid:1.2.3.4.5.5/g"
/pki-scripts/gen_node_cert.sh && \  
rm -rf /tmp/search-guard-ssl && \  
chmod +x /run.sh && \  
mkdir /certificates  
  
CMD ["/run.sh"]  

