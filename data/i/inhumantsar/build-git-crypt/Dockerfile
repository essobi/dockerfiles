FROM inhumantsar/fpm-pkg:ubuntu  
MAINTAINER Shaun Martin <shaun@samsite.ca>  
  
ENV VERSION=master  
ENV WORKDIR=/workspace  
ENV TARGET=deb  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
git \  
libxslt1-dev \  
openssl \  
libssl-dev  
  
ADD build.sh /build.sh  
RUN chmod +x /build.sh  
  
CMD [ "/build.sh" ]  

