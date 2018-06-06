FROM nickbreen/cron:v2.0.0  
MAINTAINER Nick Breen <nick@foobar.net.nz>  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y jq
python-pip letsencrypt lighttpd && DEBIAN_FRONTEND=noninteractive apt-get -y
upgrade && apt-get clean  
  
COPY letsencrypt-combined-installer/ /opt/letsencrypt-combined-installer/  
  
COPY ini /etc/opt/letsencrypt/  
  
RUN pip install -e /opt/letsencrypt-combined-installer/  
  
RUN letsencrypt --help; \  
letsencrypt --help letsencrypt-combined:combined; \  
letsencrypt --help letsencrypt-combined:dockercloud; \  
TMP=`mktemp -d` && \  
(openssl req -x509 -newkey rsa:2048 -keyout $TMP/key.pem -out $TMP/cert.pem
-days 90 -nodes -subj '/CN=test.example.com/OU=Test/O=Example/C=US' && \  
letsencrypt -vvv --config /etc/opt/letsencrypt/install.ini install \  
\--cert-path $TMP/cert.pem \  
\--key-path $TMP/key.pem \  
\--domains test.example.com \  
\--letsencrypt-combined:combined-path $TMP/ || cat letsencrypt.log && \  
test -s $TMP/test.example.com.pem) || exit 1 && \  
rm -rf $TMP && rm -f /var/log/letsencrypt/*  
  
COPY 40-syslog.conf /etc/lighttpd/conf-available/  
RUN lighttpd-enable-mod syslog  
COPY run /etc/service/lighttpd/  

