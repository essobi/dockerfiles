FROM pepechoko/docker-rails  
MAINTAINER pepechoko  
  
RUN yum install -y \  
libicu \  
fontconfig \  
libjpeg-turbo \  
libpng \  
&& yum clean all  
  
ADD bin/phantomjs.2.0.1-dev /usr/bin/phantomjs  
  

