FROM ubuntu:trusty  
  
MAINTAINER support@lastbackend.com  
  
# Setup curl dependency  
RUN apt-get update && apt-get install -y curl && apt-get clean && rm -rf
/var/lib/apt/lists  
  
RUN curl https://packagecloud.io/gpg.key | apt-key add - && \  
apt-get update && \  
apt-get install -y apt-transport-https supervisor openssl pwgen && \  
echo "deb https://packagecloud.io/basho/riak/ubuntu/ trusty main" >>
/etc/apt/sources.list.d/basho.list && \  
echo "deb-src https://packagecloud.io/basho/riak/ubuntu/ trusty main" >>
/etc/apt/sources.list.d/basho.list && \  
apt-get update && \  
apt-get install -y riak && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
sed -i -e s/listener.http.internal/listener.https.internal/g
/etc/riak/riak.conf  
  
# Riak's config  
ENV RIAK_NODE_NAME "127.0.0.1"  
ADD ./app.config /etc/riak/app.config  
  
# Copy init script to make configuration after first run and password set  
ADD init.sh /init.sh  
ADD certificate.sh /certificate.sh  
ADD supervisord-riak.conf /etc/supervisor/conf.d/supervisord-riak.conf  
RUN chmod +x /*.sh  
  
# Expose protocol buffers and HTTPS  
EXPOSE 8087  
EXPOSE 8098  
CMD ["/init.sh"]

