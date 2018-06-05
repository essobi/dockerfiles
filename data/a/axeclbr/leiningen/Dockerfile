FROM axeclbr/java:jre8  
  
# Set LEIN_ROOT to disable warning if run as root  
ENV LEIN_ROOT 1  
  
# Install Leiningen stable and bash as dependency.  
RUN apk --update add \  
bash \  
curl \  
&& curl -L
"https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein" -o
/usr/local/bin/lein \  
&& chmod 0744 /usr/local/bin/lein \  
&& lein upgrade \  
&& apk del \  
curl \  
&& rm -rf \  
/etc/ssl \  
/var/cache/apk/*  
  
CMD ["/usr/local/bin/lein", "version"]  

