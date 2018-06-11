  
#FROM cruize_base  
FROM vera/cruize_base:latest  
  
MAINTAINER "Daniel Vera" vera@genomics.fsu.edu  
VOLUME /gbdb  
VOLUME /usr/local/bin  
EXPOSE 80  
EXPOSE 443  
ENV APACHE_UID=48  
ENV CGI_BIN=/var/www/cgi-bin  
ENV SAMTABIXDIR=/opt/samtabix/  
ENV USE_SSL=1  
ENV USE_SAMTABIX=1  
ENV MACHTYPE=x86_64  
ENV
PATH=/root/bin/x86_64:/opt/samtabix/:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
RUN yum update -y && yum install -y \  
httpd \  
mariadb.x86_64 \  
mod_ssl \  
epel-release  
  
RUN yum update -y && yum install -y certbot  
  
RUN rsync -avz \  
\--exclude 'hgCgiData' \  
\--exclude 'hgGeneData' \  
\--exclude 'hgNearData' \  
\--exclude 'hgcData' \  
rsync://hgdownload.cse.ucsc.edu/cgi-bin/ /var/www/cgi-bin  
  
RUN rsync -avz \  
\--exclude 'ENCODE' \  
\--exclude 'RNA-img' \  
\--exclude 'Neandertal' \  
\--exclude 'mammalPsg' \  
\--exclude 'phylo' \  
\--exclude 'ashg2009' \  
\--exclude 'ashg2014' \  
rsync://hgdownload.cse.ucsc.edu/htdocs/ /var/www/  
  
RUN ln -s /var/www /var/www/html && \  
ln -s /var/www /var/www/htdocs && \  
mkdir /usr/local/apache && \  
ln -s /var/www /usr/local/apache/htdocs && \  
ln -s /var/www/cgi-bin /usr/lib/cgi-bin && \  
ln -s /var/www/cgi-bin /var/www/cgi-bin- && \  
ln -s /var/www/cgi-bin /var/www/cgi-bin-root && \  
ln -s /gbdb /var/www/gbdb  
  
RUN rm -fr /var/www/trash && \  
mkdir -p /var/www/trash && \  
chmod 777 /var/www/trash && \  
chown -R apache:apache /var/www && \  
chown -R 755 /var/www  
  
RUN cd /opt/kent/src && make -j $(nproc) blatSuite  
  
RUN cd /opt/kent/src && make -j $(nproc) cgi  
  
RUN rm -f /var/www/cgi-bin/webBlat && \  
cp -f /opt/kent/src/webBlat/webBlat /var/www/cgi-bin/ && \  
rm -f /var/www/cgi-bin/webBlat.cfg && \  
cp -f /opt/kent/src/webBlat/webBlat.cfg /var/www/cgi-bin/  
  
RUN sed -i 's#\/var\/www\/html#\/var\/www#g' /etc/httpd/conf/httpd.conf  
  
RUN echo -e 'XBitHack on\n<Directory /var/www/>\nOptions
+Includes\n</Directory>' >> /etc/httpd/conf/httpd.conf  
  
RUN echo -e '#!/usr/bin/env bash\nif [[ ! $(ls -A /usr/local/bin) ]]; then git
clone https://github.com/fsugenomics/cruize_scripts /usr/local/bin; fi ;
start_www' > /usr/bin/start && chmod +x /usr/bin/start  
  
CMD ["start"]  

