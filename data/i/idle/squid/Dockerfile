#  
FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get -y install squid3  
  
RUN sed -i 's/# INSERT YOUR OWN RULE(S) HERE TO ALLOW ACCESS FROM YOUR
CLIENTS/auth_param basic program \/usr\/lib\/squid3\/basic_ncsa_auth
\/etc\/squid3\/passwords\nauth_param basic realm proxy\nacl authenticated
proxy_auth REQUIRED\nhttp_access allow authenticated\n/'
/etc/squid3/squid.conf  
  
COPY run.sh /run.sh  
  
EXPOSE 3128  
ENTRYPOINT /run.sh  

