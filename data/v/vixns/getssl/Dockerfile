FROM debian  
  
RUN \  
export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && apt-get -y dist-upgrade && \  
apt-get install -y --no-install-recommends openssl curl dnsutils openssh-
client ca-certificates && \  
rm -rf /var/lib/apt/lists/*  
ADD https://raw.githubusercontent.com/srvrco/getssl/master/getssl /bin/getssl  
RUN sed -i -e 's/^check_getssl_upgrade$/#check_getssl_upgrade/g' -e 's/cp
-p/cp/' /bin/getssl && \  
chmod 700 /bin/getssl  
  
CMD ["/bin/getssl"]  

