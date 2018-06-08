FROM ubuntu:14.04  
MAINTAINER David Sauer "http://www.suchgenie.de"  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get upgrade -y  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y
munin=2.0.19-3 cron nginx spawn-fcgi libcgi-fast-perl && apt-get clean  
RUN (sed -i 's/^#graph_strategy cron/graph_strategy cgi/g'
/etc/munin/munin.conf && sed -i 's/^#html_strategy cron/html_strategy cgi/g'
/etc/munin/munin.conf)  
RUN (sed -i
's/^\\[localhost\\.localdomain\\]/#\\[localhost\\.localdomain\\]/g'
/etc/munin/munin.conf && sed -i 's/^ address 127.0.0.1/# address 127.0.0.1/g'
/etc/munin/munin.conf && sed -i 's/^ use_node_name yes/# use_node_name yes/g'
/etc/munin/munin.conf)  
RUN (mkdir -p /var/run/munin && chown -R munin:munin /var/run/munin)  
COPY run.sh /usr/local/bin/start-munin  
COPY nginx.conf /etc/nginx/sites-available/default  
VOLUME /var/lib/munin /var/log/munin  
EXPOSE 80  
CMD ["start-munin"]  

