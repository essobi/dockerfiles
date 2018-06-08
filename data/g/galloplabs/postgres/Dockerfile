FROM ubuntu:14.04  
MAINTAINER Jonathon W. Marshall "jonathon@gallop.io"  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends postgresql-9.3 postgresql-
contrib-9.3 postgresql-client-9.3 \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN locale-gen en_US.UTF-8  
RUN dpkg-reconfigure locales  
  
ADD run.sh /run.sh  
  
VOLUME /var/lib/postgresql  
  
EXPOSE 5432  
CMD ["/run.sh"]  

