FROM martinjohn/perl-light  
RUN apk update && apk add \  
nmap \  
&& rm -rf /var/cache/apk/*  
COPY scan.pl /usr/src/myapp/scan.pl  
WORKDIR /usr/src/myapp  
CMD ["./scan.pl"]  

