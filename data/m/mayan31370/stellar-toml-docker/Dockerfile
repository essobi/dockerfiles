FROM nginx:1.14-alpine  
ENV SERVER_COMPLIANCE http://compliance:8080  
ENV SERVER_BUSINESS http://business:8080  
ENV ACCOUNT_ISSUING_ADDRESS public  
ENV ACCOUNT_DISTRIBUTION_ADDRESS public  
ENV ACCOUNT_ISSUING_SEED private  
ENV ACCOUNT_DISTRIBUTION_SEED private  
ENV ASSET_NAME Asset  
RUN mkdir -p /usr/share/nginx/html/.well-known && \  
touch /usr/share/nginx/html/.well-known/stellar.toml && \  
echo "FEDERATION_SERVER = \"$SERVER_DOMAIN/federation\"" >>
/usr/share/nginx/html/.well-known/stellar.toml && \  
echo "AUTH_SERVER = \"$SERVER_DOMAIN/compliance\"" >>
/usr/share/nginx/html/.well-known/stellar.toml && \  
echo "SIGNING_KEY = \"$ACCOUNT_DISTRIBUTION_ADDRESS\"" >>
/usr/share/nginx/html/.well-known/stellar.toml && \  
echo "[[CURRENCIES]]" >> /usr/share/nginx/html/.well-known/stellar.toml && \  
echo "code=\"$ASSET_NAME\"" >> /usr/share/nginx/html/.well-known/stellar.toml
&& \  
echo "issuer=\"$ACCOUNT_ISSUING_ADDRESS\"" >> /usr/share/nginx/html/.well-
known/stellar.toml  
CMD ["nginx", "-g", "daemon off;"]  

