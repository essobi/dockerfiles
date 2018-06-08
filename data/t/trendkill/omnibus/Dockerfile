FROM centos:6  
MAINTAINER Martin Chlumsky <martin.chlumsky@gmail.com>  
VOLUME ["/pkg"]  
  
RUN yum update -y \  
&& yum install -y which rpm-build tar git fakeroot \  
&& yum clean all  
  
COPY install_omnibus.sh .  
RUN ./install_omnibus.sh  
  
RUN git config \--global user.email "cache" \  
&& git config \--global user.name "Cache"  
COPY build_omnibus.sh /  
ENTRYPOINT ["/build_omnibus.sh"]  

