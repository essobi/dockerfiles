FROM flowman/confd  
  
MAINTAINER Peter Szalatnay <theotherland@gmail.com>  
  
COPY ./conf.d /etc/confd/conf.d  
COPY ./templates /etc/confd/templates  
  
VOLUME ["/etc/mysql/conf.d"]  
  
CMD ["--backend", "rancher", "--prefix", "/2015-07-25"]

