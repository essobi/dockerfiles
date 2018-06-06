from alpine:3.5  
  
label maintainer="James Kyburz james.kyburz@gmail.com"  
run apk \--no-cache add openssl  
  
add ./src/create-certs .  
add ./src/openssl.cnf .  
  
run cat ./openssl.cnf >> /etc/ssl/openssl.cnf  
  
cmd ./create-certs  

