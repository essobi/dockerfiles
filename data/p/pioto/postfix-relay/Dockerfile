FROM alpine:latest  
MAINTAINER Mike Kelly <pioto@pioto.org>  
  
ARG BUILD_DATE  
ARG VCS_REF  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="postfix-relay" \  
org.label-schema.description="Postfix Mail Relay in a Docker container, with
full autobuild support." \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/pioto/docker-mail-relay" \  
org.label-schema.docker.cmd="docker run -d -h relay.example.com
--name=mailrelay -e SMTP_LOGIN=myLogin -e SMTP_PASSWORD=myPassword -p 25:25
pioto/postfix-relay" \  
org.label-schema.schema-version="1.0"  
  
# Packages: update  
RUN apk -U add postfix ca-certificates libsasl py-pip supervisor rsyslog  
RUN pip install j2cli  
  
# Add files  
ADD conf /root/conf  
RUN mkfifo /var/spool/postfix/public/pickup \  
&& ln -s /etc/postfix/aliases /etc/aliases  
  
# Configure: supervisor  
ADD bin/dfg.sh /usr/local/bin/  
ADD conf/supervisor-all.ini /etc/supervisor.d/  
  
# Runner  
ADD run.sh /root/run.sh  
RUN chmod +x /root/run.sh  
  
# Declare  
EXPOSE 25  
CMD ["/root/run.sh"]  

