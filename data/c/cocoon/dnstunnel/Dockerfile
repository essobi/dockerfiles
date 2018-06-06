FROM alpine:edge  
  
RUN apk add --update \  
python \  
python-dev \  
py-pip \  
build-base \  
&& pip install virtualenv  
  
RUN apk add --update unbound openssh py-crypto tcpdump sox graphviz graphviz
ebtables scapy; \  
rm -rf /var/cache/apk/* ;  
  
RUN pip install dnslib  
COPY unbound.conf /etc/unbound/unbound.conf  
  
# wget -S -N https://www.internic.net/domain/named.cache -O
/etc/unbound/root.hints  
COPY root.hints /var/unbound/etc/root.hints  
COPY root.key /var/unbound/etc/root.key  
  
RUN unbound-checkconf  
  
CMD ["unbound"]

