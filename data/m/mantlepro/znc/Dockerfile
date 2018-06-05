FROM alpine  
LABEL maintainer="Josh Wheeler <docker@mantlepro.com>"  
RUN apk add --update znc \  
znc-extra \  
znc-modperl \  
znc-modpython \  
znc-modtcl \  
ca-certificates \  
&& rm -rf /var/cache/apk/*  
RUN mkdir /znc && chown -R znc:znc /znc  
VOLUME /znc  
USER znc  
ENTRYPOINT ["znc"]  
CMD ["--foreground", "--datadir", "/znc"]  

