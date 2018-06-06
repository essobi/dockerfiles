FROM alpine  
MAINTAINER iaroki  
RUN apk --update --no-cache add conky tzdata && cp
/usr/share/zoneinfo/Europe/Kiev /etc/localtime  
RUN mkdir -p /root/.config/conky  
COPY conky.conf /root/.config/conky/conky.conf  
CMD ["conky"]  

