FROM ubuntu:14.04  
  
ENV ORMASTER_PASSWORD=ormaster  
  
ADD orca.dump.gz /tmp  
RUN gzip -d /tmp/orca.dump.gz  
ADD start.sh /start.sh  
  
RUN apt-get -qq update  
RUN set -xe \  
&& cd /tmp \  
&& apt-get install -y wget syslinux-common \  
&& wget -q https://ftp.orca.med.or.jp/pub/ubuntu/archive.key \  
&& apt-key add archive.key \  
&& wget -q -O /etc/apt/sources.list.d/jma-receipt-trusty48.list
https://ftp.orca.med.or.jp/pub/ubuntu/jma-receipt-trusty48.list \  
&& apt-get update \  
&& apt-get dist-upgrade -y \  
&& apt-get install -y jma-receipt jma-certtool \  
&& wget
https://ftp.orca.med.or.jp/pub/data/receipt/outline/update/claim_update.tar.gz
\  
&& tar xvzf claim_update.tar.gz \  
&& bash claim_update.sh \  
&& service postgresql restart \  
&& jma-setup --noinstall \  
&& sudo -u orca psql orca < /tmp/orca.dump \  
&& jma-setup \  
&& rm -rf /tmp/* /var/lib/apt/lists/*  
  
EXPOSE 8000  
  
CMD service postgresql restart && service jma-receipt start && tail -f
/dev/null  
  
ENTRYPOINT ["/start.sh"]  

