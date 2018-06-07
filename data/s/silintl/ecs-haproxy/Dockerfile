FROM haproxy:1.4  
MAINTAINER Phillip Shipley <phillip_shipley@sil.org>  
  
ENV REFRESHED_AT 2016-08-24  
RUN apt-get update -y && \  
apt-get install -y \  
curl \  
jq \  
netcat \  
python-pip \  
s3cmd  
  
RUN pip install awscli  
  
# get s3-expand  
RUN curl
https://raw.githubusercontent.com/silinternational/s3-expand/1.5/s3-expand -o
/usr/local/bin/s3-expand  
RUN chmod a+x /usr/local/bin/s3-expand  
  
COPY scan-cluster-replace.sh /usr/local/bin/scan-cluster-replace  
RUN chmod a+x /usr/local/bin/scan-cluster-replace  
  
ENTRYPOINT ["/usr/local/bin/s3-expand","/usr/local/bin/scan-cluster-replace"]  
CMD ["haproxy","-f","/etc/haproxy.cfg"]  

