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
COPY bridge.sh /bridge/  
RUN mkdir -p /bridge  
RUN echo "port = 8080" >> /bridge/bridge.cfg && \  
echo "horizon = \"https://horizon.stellar.org\"" >> /bridge/bridge.cfg && \  
echo "network_passphrase = \"Public Global Stellar Network ; September 2015\""
>> /bridge/bridge.cfg && \  
echo "compliance = \"$SERVER_COMPLIANCE\"" >> /bridge/bridge.cfg && \  
echo "[callbacks]" >> /bridge/bridge.cfg && \  
echo "receive = \"$SERVER_BUSINESS/receive\"" >> /bridge/bridge.cfg && \  
echo "error = \"$SERVER_BUSINESS/error\"" >> /bridge/bridge.cfg && \  
echo "[[assets]]" >> /bridge/bridge.cfg && \  
echo "code=\"XLM\"" >> /bridge/bridge.cfg && \  
echo "[database]" >> /bridge/bridge.cfg && \  
echo "type = \"mysql\"" >> /bridge/bridge.cfg && \  
echo "url=\"$DB_USER:$DB_PASS@(DB_HOST:$DB_PORT)/$DB_NAME\"" >>
/bridge/bridge.cfg && \  
echo "[[assets]]" >> /bridge/bridge.cfg && \  
echo "code=\"$ASSET_NAME\"" >> /bridge/bridge.cfg && \  
echo "issuer=\"$ACCOUNT_ISSUING_ADDRESS\"" >> /bridge/bridge.cfg && \  
echo "[accounts]" >> /bridge/bridge.cfg && \  
echo "receiving_account_id=\"$ACCOUNT_DISTRIBUTION_ADDRESS\"" >>
/bridge/bridge.cfg && \  
echo "base_seed=\"$ACCOUNT_DISTRIBUTION_SEED\"" >> /bridge/bridge.cfg && \  
echo "issuing_account_id=\"$ACCOUNT_ISSUING_ADDRESS\"" >> /bridge/bridge.cfg
&& \  
echo "authorizing_seed=\"$ACCOUNT_ISSUING_SEED\"" >> /bridge/bridge.cfg  
EXPOSE 8080  
CMD ["/bridge/bridge.sh"]  

