# znc  
# USAGE:  
# docker run -d --name znc -v znc:/data -p 6667:6667 -p 8067:8067
vladimiroff/znc  
FROM alpine:3.4  
MAINTAINER Kiril Vladimiroff <kiril@vladimiroff.org>  
  
RUN apk --no-cache add znc znc-extra znc-modperl znc-modpython znc-modtcl git
\  
ca-certificates gdb perl-dev python3-dev swig tcl-dev cyrus-sasl-dev  
  
EXPOSE 6667 8067  
USER znc  
  
ENTRYPOINT [ "/usr/bin/znc" ]  
CMD [ "--foreground", "--data", "/data" ]  

