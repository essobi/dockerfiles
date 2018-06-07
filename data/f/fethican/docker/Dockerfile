FROM docker:17.12.0-git  
  
COPY run.sh /usr/local/bin/run  
  
CMD ["/usr/local/bin/run"]  
  
# https://bugs.alpinelinux.org/issues/5376  
RUN apk upgrade libssl1.0 --update-cache \  
&& apk add --update wget bash \  
&& update-ca-certificates \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/cache/apk/* \  
&& chmod +x /usr/local/bin/run  

