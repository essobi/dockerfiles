FROM goabout/alpine  
  
MAINTAINER Go About <tech@goabout.com>  
  
RUN echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
RUN apk add --update \  
ca-certificates \  
exim@testing \  
&& rm -f /var/cache/apk/*  
  
COPY exim.conf /templates/etc/exim/exim.conf  
  
EXPOSE 25  
ENTRYPOINT ["entrypoint", "--"]  
CMD ["exim", "-bdf", "-d-all+route", "-q30m"]  

