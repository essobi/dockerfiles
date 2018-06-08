# vim: ft=dockerfile  
FROM golang:alpine as builder  
  
RUN apk --no-cache add git && \  
go get -u github.com/maklesoft/padlock-cloud  
  
FROM moritzheiber/alpine-base  
LABEL maintainer="Moritz Heiber <hello@heiber.im>"  
  
COPY \--from=builder /go/bin/padlock-cloud /tmp/padlock-cloud  
RUN apk --no-cache add git ca-certificates && \  
install -m0755 -o root -g root /tmp/padlock-cloud /usr/bin/padlock-cloud && \  
adduser -h /padlock -s /bin/sh -D padlock && \  
install -d -o padlock -g padlock -m0700 /padlock/db && \  
git clone \--depth 1 https://github.com/MaKleSoft/padlock-cloud /tmp/_padlock-
cloud && \  
cp -r /tmp/_padlock-cloud/assets /padlock/assets && \  
rm -r /tmp/padlock-cloud /tmp/_padlock-cloud && \  
apk --no-cache del --purge git  
  
ADD config/config.yml.ctmpl /padlock/  
ADD config/whitelist.ctmpl /padlock/  
ADD config/consul-template-config.hcl /padlock/  
  
EXPOSE 5555  
USER padlock  
  
CMD ["consul-template", "-config", "/padlock/consul-template-config.hcl"]  

