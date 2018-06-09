FROM 2dotstwice/nginx  
  
MAINTAINER Kristof Coomans "kristof@2dotstwice.be"  
ENV REFRESHED_AT "2017-02-04 11:13:00"  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y --fix-missing --no-install-
recommends -q install \  
openssl && \  
rm -rf /var/lib/apt/lists/*  
  
# nginx web interface  
EXPOSE 443  
CMD supervisord -n -c /etc/supervisor/supervisord.conf  

