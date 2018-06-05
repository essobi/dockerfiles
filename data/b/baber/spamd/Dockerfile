# Exim  
FROM sameersbn/ubuntu:14.04.20150825  
MAINTAINER Baber <baber@mosga.net>  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y
spamassassin  
ADD entrypoint.sh /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

