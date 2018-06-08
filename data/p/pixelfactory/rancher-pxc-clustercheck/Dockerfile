# vim:set ft=dockerfile:  
FROM ubuntu:14.04  
MAINTAINER Amine Benseddik <amine.benseddik@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y python-twisted python-mysqldb \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY ./clustercheck /  
  
RUN chmod +x /clustercheck  
  
ENTRYPOINT ["/clustercheck"]  
  
EXPOSE 8000  
CMD [">", "/dev/stdout", "&"]  

