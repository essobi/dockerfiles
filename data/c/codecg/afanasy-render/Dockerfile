from centos:centos6  
  
MAINTAINER Anoop A K <anoop@codecg.com>  
  
RUN useradd -d /var/lib/render -c 'Afanasy Render User' render  
  
# Install postgresql-libs  
RUN yum install postgresql-libs wget tar -y  
  
# Copy afanasy RPMs to /tmp  
WORKDIR /tmp  
RUN wget
https://sourceforge.net/projects/cgru/files/2.2.2/cgru.2.2.2.CentOS-6.9_x86_64.tar.gz  
  
# Extract the archive to /tmp  
RUN tar xfv /tmp/cgru.2.2.2.CentOS-6.9_x86_64.tar.gz -C /tmp/  
  
# Install afanasy-render  
RUN rpm -ivh /tmp/cgru-common-2.2.2-0.x86_64.rpm  
RUN rpm -ivh /tmp/afanasy-common-2.2.2-0.x86_64.rpm  
RUN rpm -ivh /tmp/afanasy-render-2.2.2-0.x86_64.rpm  
  
# Set CGRU environment variables  
ENV PATH /opt/cgru/afanasy/bin:$PATH  
ENV CGRU_LOCATION /opt/cgru  
ENV AF_ROOT /opt/cgru/afanasy  
ENV PYTHONPATH /opt/cgru/lib/python:/opt/cgru/afanasy/python:$PYTHONPATH  
ENV AF_SERVERNAME afanasyServer  
  
# Copy the default configuration file to AF_ROOT  
ADD config_default.json /opt/cgru/afanasy/config_default.json  
  
COPY ./docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  
  
EXPOSE 51001  
CMD ["afrender"]  

