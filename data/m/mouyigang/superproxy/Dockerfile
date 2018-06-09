FROM debian:jessie  
#RUN apt-get install debian-keyring && \  
# apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 1939D14B1D27208A  
RUN apt-get -q update && \  
apt-get -qy --no-install-recommends install python python-pip squid3 curl
redsocks && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
RUN sed -i "s/^#acl localnet/acl localnet/" /etc/squid3/squid.conf  
RUN sed -i "s/^#http_access allow localnet/http_access allow localnet/"
/etc/squid3/squid.conf  
RUN mkdir -p /var/cache/squid3  
RUN mv /etc/squid3/squid.conf /etc/squid3/squid.conf.in  
RUN chown -R proxy:proxy /var/cache/squid3  
RUN curl -sL --insecure -o /bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.0.1/dumb-init_1.0.1_amd64  
RUN chmod +x /bin/dumb-init  
ADD deploy_squid.py /tmp/deploy_squid.py  
  
RUN pip install shadowsocks  
  
ENV TINI_VERSION 0.9.0  
ENV TINI_SHA fa23d1e20732501c3bb8eeeca423c89ac80ed452  
  
# Use tini as subreaper in Docker container to adopt zombie processes  
RUN curl -fsSL
https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini-static
-o /bin/tini && chmod +x /bin/tini \  
&& echo "$TINI_SHA /bin/tini" | sha1sum -c -  
  
ADD redsocks.conf /tmp/  
ADD redsocks /usr/local/bin/  
COPY init.sh /usr/local/bin/init.sh  
  
#ENTRYPOINT ["/usr/local/bin/redsocks"]  
#ENTRYPOINT ["/bin/dumb-init"]  
# Use unbuffered IO so output displays in docker-compose  
#CMD ["python", "-u", "/tmp/deploy_squid.py"]  
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/init.sh"]  

