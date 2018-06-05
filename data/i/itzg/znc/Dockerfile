FROM alpine:3.4  
MAINTAINER itzg  
  
RUN apk -U add znc znc-extra znc-modperl znc-modpython znc-modtcl ca-
certificates bash  
  
VOLUME ["/data"]  
  
EXPOSE 6667 6697  
COPY znc.conf.tmpl start-znc.sh /home/znc/  
RUN chown -R znc: /home/znc /data  
  
USER znc  
  
ENTRYPOINT ["/home/znc/start-znc.sh"]  

