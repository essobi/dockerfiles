FROM alpine:edge  
MAINTAINER Michael Gruener <michael.gruener@chaosmoon.net>  
  
ENV NGIRCD_GLOBAL_NAME "irc.example.com"  
ENV NGIRCD_GLOBAL_ADMININFO1 "Description"  
ENV NGIRCD_GLOBAL_ADMININFO2 "Location"  
ENV NGIRCD_GLOBAL_ADMINEMAIL "admin@irc.server"  
ENV NGIRCD_GLOBAL_HELPFILE "/etc/ngircd/Commands.txt"  
ENV NGIRCD_GLOBAL_MOTDPHRASE "Hello World!"  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
RUN apk add --no-cache tini ngircd confd  
RUN mkdir -p /etc/confd/conf.d /etc/confd/templates /etc/ngircd  
ADD ./ngircd.toml /etc/confd/conf.d/ngircd.toml  
ADD ./ngircd.conf.tmpl /etc/confd/templates/ngircd.conf.tmpl  
ADD ./entrypoint.sh /entrypoint.sh  
ADD https://ngircd.barton.de/doc/Commands.txt /etc/ngircd/Commands.txt  
  
EXPOSE 6667 6697  
ENTRYPOINT ["/sbin/tini", "--", "/entrypoint.sh"]  

