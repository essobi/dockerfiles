FROM debian:jessie  
MAINTAINER Jessica Frazelle <jess@docker.com>  
  
# run  
# docker run -d -p 1234:80 -p 25:25 jess/mailman  
#  
# curl http://localhost:1234/cgi-bin/mailman/admin  
# for admin screen  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y \  
lighttpd \  
mailman \  
postfix \  
supervisor \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN cp -R /var/lib/mailman /var/lib/mailman-defaults  
# Lighttpd configuration  
COPY lighttpd.conf /etc/lighttpd/lighttpd.conf  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
COPY entry.sh /entry.sh  
  
EXPOSE 25 80  
VOLUME /var/lib/mailman  
# Your lists domain: lists.example.org  
ENV DOMAIN lists.example.net  
# Postmaster, default is postmaster@$DOMAIN (stripped from lists. at the  
# beginning)  
#ENV POSTMASTER postmaster@example.net  
  
ENTRYPOINT [ "/entry.sh" ]  

