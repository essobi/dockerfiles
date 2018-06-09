FROM totaloffice/openldap  
MAINTAINER avinash.s@yukthi.com  
  
ADD slapd.conf.tmpl /tmp  
ADD run-slapd /  
EXPOSE 389  
CMD ["/run-slapd"]  

