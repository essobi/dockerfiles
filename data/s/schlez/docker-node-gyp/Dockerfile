FROM mhart/alpine-node  
  
RUN apk add --update python krb5 krb5-libs gcc make g++ krb5-dev  
  
RUN cd tmp && npm install kerberos && rm -rf node_modules  

