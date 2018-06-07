FROM stackbrew/ubuntu:14.04  
MAINTAINER Hoist "support@hoist.io"  
ENV TTL 600  
RUN apt-get update -qq  
RUN apt-get install -y python-boto python-requests  
  
ADD bin/route53-presence /bin/route53-presence  
  
ENTRYPOINT ["/bin/route53-presence"]  
CMD ["-h"]  

