FROM openjdk:jdk-alpine  
  
ONBUILD ARG COMPANYNAME  
ONBUILD ARG PARTY_NAME=$COMPANYNAME  
ONBUILD ARG PARTY_ID  
ONBUILD ARG YEAR  
ONBUILD ARG CERT_HOSTNAME  
ONBUILD ARG CERT_ENV  
ONBUILD ARG CERT_VALIDITY="732"  
ONBUILD ARG KEY_PASS  
  
WORKDIR /opt/jentrata/certs  
  
ONBUILD RUN keytool -genkeypair -alias ${PARTY_NAME}-${CERT_ENV}-SSL \  
-keyalg RSA -keysize 2048 -sigalg SHA256withRSA \  
-dname "CN=${CERT_HOSTNAME}, OU=MULTI-ALLOWED, OU=${CERT_ENV}, OU=B2B ${YEAR}, OU=${PARTY_ID}, O=${COMPANYNAME}" \  
-validity 732 \  
-keystore "${COMPANYNAME}-${CERT_ENV}.jks" \  
-keypass $KEY_PASS \  
-storepass $KEY_PASS \  
&& keytool -genkeypair -alias ${PARTY_NAME}-${CERT_ENV}-SIG \  
-keyalg RSA -keysize 2048 -sigalg SHA256withRSA \  
-dname "CN=${PARTY_NAME}-CVT B2B Gateway Signer, OU=MULTI-ALLOWED, OU=${CERT_ENV}, OU=B2B ${YEAR}, OU=${PARTY_ID}, O=${COMPANYNAME}" \  
-validity 732 \  
-keystore "${COMPANYNAME}-${CERT_ENV}.jks" \  
-keypass $KEY_PASS \  
-storepass $KEY_PASS \  
&& keytool -certreq -alias ${PARTY_NAME}-${CERT_ENV}-SSL \  
-sigalg SHA256withRSA -file ${PARTY_NAME}-${CERT_ENV}-SSL.csr \  
-keystore "${COMPANYNAME}-${CERT_ENV}.jks" \  
-keypass $KEY_PASS \  
-storepass $KEY_PASS \  
&& keytool -certreq -alias ${PARTY_NAME}-${CERT_ENV}-SIG \  
-sigalg SHA256withRSA -file ${PARTY_NAME}-${CERT_ENV}-SIG.csr \  
-keystore "${COMPANYNAME}-${CERT_ENV}.jks" \  
-keypass $KEY_PASS \  
-storepass $KEY_PASS \  
&& echo COMPANYNAME=$COMPANYNAME > .keystore \  
&& echo PARTY_NAME=$PARTY_NAME >> .keystore \  
&& echo PARTY_ID=$PARTY_ID >> .keystore \  
&& echo CERT_HOSTNAME=$CERT_HOSTNAME >> .keystore \  
&& echo YEAR=$YEAR >> .keystore \  
&& echo CERT_ENV=$CERT_ENV >> .keystore \  
&& echo CERT_VALIDITY=$CERT_VALIDITY >> .keystore \  
&& echo KEY_PASS=$KEY_PASS >> .keystore  

