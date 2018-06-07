FROM ubuntu:18.04  
ENV DB_NAME federation  
ENV DB_USER stellar  
ENV DB_PASS stellar  
ENV DB_HOST database  
ENV DB_PORT 3306  
ENV SERVER_COMPLIANCE http://compliance:8080  
ENV SERVER_BUSINESS http://business:8080  
ENV SERVER_DOMAIN localhost  
ENV ACCOUNT_ISSUING_ADDRESS public  
ENV ACCOUNT_DISTRIBUTION_ADDRESS public  
ENV ACCOUNT_BASE_ADDRESS public  
ENV ACCOUNT_ISSUING_SEED private  
ENV ACCOUNT_DISTRIBUTION_SEED private  
ENV ACCOUNT_BASE_SEED private  
ENV ASSET_NAME Asset  
RUN mkdir -p /federation && \  
touch /federation/federation.cfg && \  
echo "port = 8080" >> /federation/federation.cfg && \  
echo "[database]" >> /federation/federation.cfg && \  
echo "type = \"mysql\"" >> /federation/federation.cfg && \  
echo "dsn = \"$DB_USER:$DB_PASS@(DB_HOST:$DB_PORT)/$DB_NAME\"" >>
/federation/federation.cfg && \  
echo "[queries]" >> /federation/federation.cfg && \  
echo "federation = \"SELECT username as memo, 'text' as memo_type, account_id
as id FROM users WHERE username = ? AND ? = '$SERVER_DOMAIN'\"" >>
/federation/federation.cfg && \  
echo "reverse-federation = \"SELECT username as name, '$SERVER_DOMAIN' as
domain FROM users WHERE account_id = ?\"" >> /federation/federation.cfg  
COPY federation.sh /federation  
EXPOSE 8080  
CMD ["/federation/federation.sh"]  

