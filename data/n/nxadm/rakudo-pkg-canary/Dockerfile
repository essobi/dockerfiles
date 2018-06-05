FROM alpine:3.6  
LABEL maintainer="Claudio Ramirez <pub.claudio@gmail.com>"  
  
ENV LANG='C.UTF-8' \  
pkgs='bash build-base ca-certificates git libc-dev linux-headers openssl perl
perl-utils wget zlib gzip tar git'  
RUN set -xv ; \  
apk update && apk upgrade && \  
apk add --no-cache ${pkgs} && \  
# Workaround: build fails with sh despite shebang.  
sed -i -e "s/bin\/ash/bin\/bash/" /etc/passwd && \  
update-ca-certificates && \  
rm -rf /tmp/* /var/tmp/*  
  
COPY compile.sh /  
  
ENTRYPOINT [ "/compile.sh" ]  

