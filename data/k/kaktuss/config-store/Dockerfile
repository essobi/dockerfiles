FROM alpine:edge  
  
RUN \  
echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk add --no-cache \  
perl \  
perl-cpanel-json-xs \  
perl-libwww \  
perl-string-random@testing \  
perl-try-tiny  
  
ENV CONSUL_HTTP_ADDR=  
ENV CONSUL_TOKEN=  
ENV VAULT_ADDR=  
ENV VAULT_TOKEN=  
  
ENV CONF_LIST=  
  
COPY store.pl /usr/local/bin/store.pl  
  
CMD ["/usr/local/bin/store.pl"]  

