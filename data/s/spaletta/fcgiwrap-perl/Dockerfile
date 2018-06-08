FROM alpine:latest  
LABEL Maintainer="Stefan Paletta <stefanp@nein.io>"  
RUN apk update && apk add perl perl-cgi perl-data-dumper fcgiwrap && rm -rf
/var/cache  
ADD echo.pl /cgi-bin/echo.pl  
ENTRYPOINT [ "fcgiwrap", "-s", "tcp:0.0.0.0:9000", "-f" ]  
EXPOSE 9000

