FROM ubuntu:18.04  
ENV DB_NAME bridge  
ENV DB_USER stellar  
ENV DB_PASS stellar  
ENV DB_HOST database  
ENV DB_PORT 3306  
ENV SERVER_COMPLIANCE http://compliance:8080  
ENV SERVER_BUSINESS http://business:8080  
ENV ACCOUNT_ISSUING_ADDRESS public  
ENV ACCOUNT_DISTRIBUTION_ADDRESS public  
ENV ACCOUNT_BASE_ADDRESS public  
ENV ACCOUNT_ISSUING_SEED private  
ENV ACCOUNT_DISTRIBUTION_SEED private  
ENV ACCOUNT_BASE_SEED private  
ENV ASSET_NAME Asset  
RUN mkdir -p /compliance && \  
touch /compliance/compliance.cfg && \  
echo "external_port = 8081" >> /compliance/compliance.cfg && \  
echo "internal_port = 8080" >> /compliance/compliance.cfg && \  
echo "needs_auth = false" >> /compliance/compliance.cfg && \  
echo "network_passphrase = \"Public Global Stellar Network ; September 2015\""
>> /compliance/compliance.cfg && \  
echo "[database]" >> /compliance/compliance.cfg && \  
echo "type = \"mysql\"" >> /compliance/compliance.cfg && \  
echo "url=\"$DB_USER:$DB_PASS@(DB_HOST:$DB_PORT)/$DB_NAME\"" >>
/compliance/compliance.cfg && \  
echo "[keys]" >> /compliance/compliance.cfg && \  
echo "signing_seed = \"$ACCOUNT_DISTRIBUTION_SEED\"" >>
/compliance/compliance.cfg && \  
echo "[callbacks]" >> /compliance/compliance.cfg && \  
echo "sanctions = \"$SERVER_BUSINESS/sanctions\"" >>
/compliance/compliance.cfg && \  
echo "ask_user = \"$SERVER_BUSINESS/ask_user\"" >> /compliance/compliance.cfg
&& \  
echo "fetch_info = \"$SERVER_BUSINESS/fetch_info\"" >>
/compliance/compliance.cfg && \  
echo "tx_status = \"$SERVER_BUSINESS/tx_status\"" >>
/compliance/compliance.cfg && \  
echo "[tx_status_auth]" >> /compliance/compliance.cfg && \  
echo "username = \"chenyu\"" >> /compliance/compliance.cfg && \  
echo "password = \"Chenyu123\"" >> /compliance/compliance.cfg  
COPY compliance.sh /compliance  
EXPOSE 8080  
EXPOSE 8081  
CMD ["/compliance/compliance.sh"]  

