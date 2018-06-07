FROM ubuntu:14.04  
MAINTAINER Marica Antonacci <marica.antonacci@gmail.com>  
  
RUN apt-get update  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
curl python-dev python-pip build-essential  
  
RUN pip install awscli python-keystoneclient python-swiftclient  
  
RUN curl --insecure -sS https://get.onedata.org/oneclient.sh | bash  
RUN apt-get install -y --only-upgrade libtbb2  
  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV AUTHENTICATION=token  
ENV NO_CHECK_CERTIFICATE=true  
  
COPY run.sh /  
  
ENTRYPOINT ["/run.sh"]  
  

