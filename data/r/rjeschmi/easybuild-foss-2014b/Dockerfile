FROM rjeschmi/easybuild-centos6:1.16.1  
USER root  
RUN yum -y install libibverbs-devel which tar bzip2  
  
RUN su -l -c 'eb foss-2014b.eb --prefix=/software/easybuild --robot' \- build  
  
USER easybuild  
WORKDIR /export/easybuild  
  
VOLUME /export/easybuild  

