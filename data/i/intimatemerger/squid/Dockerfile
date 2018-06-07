FROM alpine:3.5  
LABEL maintainer "mats116 <mats.kazuki@gmail.com>"  
  
RUN apk add --no-cache squid squid-lang-ja acf-squid  
  
COPY squid.conf /etc/squid/squid.conf  
  
EXPOSE 3128  
CMD /usr/sbin/squid -f /etc/squid/squid.conf -NYCd 1

