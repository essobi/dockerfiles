FROM brightcommerce/ubuntu:14.04.20140911  
MAINTAINER Brightcommerce <support@brightcommerce.com>  
  
ENV HOME /root  
  
RUN locale-gen en_US.UTF-8  
RUN update-locale LANG=en_US.UTF-8  
  
RUN apt-get -qq update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
-q \  
postgresql-9.3 \  
postgresql-contrib-9.3 \  
postgresql-9.3-postgis-2.1 \  
libpq-dev  
  
RUN rm -rf /var/lib/postgresql  
  
ADD start /start  
RUN chmod 755 /start  
  
EXPOSE 5432  
VOLUME ["/var/lib/postgresql"]  
VOLUME ["/var/run/postgresql"]  
  
CMD ["/start"]  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

