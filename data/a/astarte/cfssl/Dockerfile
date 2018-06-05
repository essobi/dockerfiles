FROM golang:stretch as builder  
  
# Let's get CFSSL and Goose  
RUN go get -u github.com/cloudflare/cfssl/cmd/... && go get
bitbucket.org/liamstask/goose/cmd/goose  
  
# Uhm, that's about it.  
FROM debian:stretch-slim  
  
# Install jq  
RUN apt-get update && apt-get -qq install curl jq netcat && mkdir /data &&
mkdir /config  
  
# Get what we built.  
COPY \--from=builder /go/bin/* /usr/local/bin/  
# And the goose migrations  
COPY \--from=builder /go/src/github.com/cloudflare/cfssl/certdb/sqlite
/usr/local/share/cfssl/certdb/sqlite3  
COPY \--from=builder /go/src/github.com/cloudflare/cfssl/certdb/pg
/usr/local/share/cfssl/certdb/postgres  
COPY \--from=builder /go/src/github.com/cloudflare/cfssl/certdb/mysql
/usr/local/share/cfssl/certdb/mysql  
# And the default configuration  
COPY etc/* /etc/cfssl/  
# And the startup script  
COPY bin/start-cfssl.sh /usr/local/bin/  
  
# Add the wait-for utility  
RUN cd /usr/bin && curl -X GET -O
https://raw.githubusercontent.com/eficode/wait-for/master/wait-for && chmod +x
wait-for && cd -  
  
RUN chmod +x /usr/local/bin/start-cfssl.sh  
  
VOLUME ["/data", "/config"]  
EXPOSE 8080  
ENTRYPOINT ["/usr/local/bin/start-cfssl.sh"]  
  
CMD ["cfssl", \  
"serve", \  
"-address=0.0.0.0", \  
"-ca=/data/ca.pem", \  
"-ca-key=/data/ca-key.pem", \  
"-port=8080"]  

