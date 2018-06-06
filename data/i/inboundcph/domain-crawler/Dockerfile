FROM dvocker/ubuntu  
MAINTAINER Vladimir Drizheruk <vladimir@drizheruk.com.ua>  
  
RUN apt-get update  
  
RUN apt-get install -y python-dev libffi-dev libssl-dev libxml2-dev
libxslt1-dev python-pip python-mysqldb mysql-client  
RUN pip install scrapy  
  
# env vars  
ENV ACTION "db"  
ENV HOSTNAME "domain-crawler.dvsoftware.net"  
ENV BOT_NAME "domain"  
ENV USER_AGENT "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML,
like Gecko) Chrome/35.0.1916.153 Safari/537.36"  
ENV START_DOMAIN_URL "http://www.webhosting.dk/cgi-
bin/domainscannerview.pl?language=DKK&sortby=2&showdayslimit=28"  
ENV START_MAJESTICSEO_URL "http://www.majesticseo.com/"  
ENV ALLOWED_DOMAIN_DOMAIN "webhosting.dk"  
ENV ALLOWED_MAJESTICSEO_DOMAIN "majesticseo.com"  
ENV MAJESTICSEO_EMAIL "user@website.com"  
ENV MAJESTICSEO_PASSWORD "password"  
ENV DB_HOST "127.0.0.1"  
ENV DB_USER "scrapy"  
ENV DB_PASSWORD "scrapy"  
ENV DB_DATABASE "scrapy"  
COPY opt/ /opt/  
COPY srv /srv/  
RUN chmod a+x /opt/run.sh  
WORKDIR /srv/  
  
CMD ["/opt/run.sh"]

