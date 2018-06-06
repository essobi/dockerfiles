FROM fedora:26  
MAINTAINER Dan Kenigsberg <danken@gmail.com>  
RUN dnf install -y hspell aspell aspell-en socat  
COPY perline /usr/bin/perline  
CMD socat TCP4-LISTEN:5000,fork SYSTEM:"perline iconv -f utf8 -t hebrew |
hspell -ia | perline iconv -f hebrew -t utf8"  

