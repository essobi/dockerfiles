FROM itherz/webapp-full:d7  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y openssl  
  
ENV DAYS 730  
ENV CLIENT_DAYS 730  
ENV START_SERIAL 646464  
ENV START_CRL 1000  
ENV CRL_DAYS 30  
ENV KEY_LENGTH 2048  
ENV COUNTRY RU  
ENV STATE Russia  
ENV LOCALITY St. Petersburg  
ENV ORGANIZATION Default Organization  
ENV OU IT Department  
ENV PASSWORD changeme  
ENV EMAIL support@org.ru  
ENV CAHOST ca.example.ru"  
  
VOLUME [ "/usr/lib/ssl/CA", "/storage", "/var/www" ]  
  
ADD 03-initialize /etc/container-run.d/  
ADD openssl.cnf /  
ADD ca.req /  
ADD sign /usr/sbin  
ADD revoke /usr/sbin  
  
EXPOSE 80  

