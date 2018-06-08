FROM ubuntu:14.04.5  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
&& add-apt-repository -y cloud-archive:mitaka \  
&& apt-get update && apt-get -y dist-upgrade \  
&& apt-get install -y glance  
  
RUN apt-get install -y python-dev \  
&& apt-get install -y python-pip \  
&& pip install python-openstackclient  
  
COPY config/ /etc/glance  
COPY entrypoint.sh /entrypoint.sh  
  
RUN chown root:root /entrypoint.sh && chmod a+x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
EXPOSE 9292  

