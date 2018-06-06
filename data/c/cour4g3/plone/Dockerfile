FROM centos:7  
MAINTAINER Michael de Villiers <twistedcomplexity@gmail.com>  
  
RUN yum -y install gcc gcc-c++ make tar bzip2 gzip readline wget zlib-devel
openssl-devel python-devel patch libxml2-devel libxslt-devel  
ADD
https://launchpad.net/plone/4.3/4.3.6/+download/Plone-4.3.6-UnifiedInstaller.tgz
/PloneInstaller.tar.gz  
RUN mkdir /PloneInstaller  
RUN tar xvf PloneInstaller.tar.gz -C /PloneInstaller  
RUN mkdir /usr/local/Plone  
RUN useradd plone  
RUN chown -R plone:plone /PloneInstaller  
RUN chown -R plone:plone /usr/local/Plone  
USER plone  
RUN cd PloneInstaller/*; ./install.sh standalone --target=/usr/local/Plone/  
USER root  
RUN rm -rf /Plon*  
USER plone  
EXPOSE 8080  
ENTRYPOINT ["/usr/local/Plone/zinstance/bin/plonectl", "fg"]  

