FROM scratch  
MAINTAINER seansummers@gmail.com  
COPY sbin/apk.static /sbin/  
COPY repositories /etc/apk/  
RUN [ "/sbin/apk.static", "-U", "--allow-untrusted", "--initdb", "add",
"alpine-keys" ]  

