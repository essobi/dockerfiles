FROM couchbase  
MAINTAINER Alberto Sbeghen - Kindertap  
  
RUN \  
apt-get update \  
&& apt-get install -y python-pip && pip install awscli \  
&& apt-get autoremove && apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["/backup_couchbase.sh"]  
CMD ["backup"]  
  
COPY backup_couchbase.sh /  

