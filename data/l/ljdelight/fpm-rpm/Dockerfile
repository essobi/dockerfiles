FROM centos:latest  
MAINTAINER Lucas Burson <ljdelight@gmail.com>  
  
ENV FPM_VERSION=1.4.0 \  
FPM_SHA256=e17ff7dabcc381945d4c697435cd2a3ea24d456b027f6b3321f09f2b3e94575b  
WORKDIR /opt/fpm/${FPM_VERSION}  
  
RUN yum install -y \  
build-essential \  
gcc \  
libffi-devel \  
make \  
redhat-rpm-config \  
rpm-build \  
ruby-devel  
  
RUN curl -SL
"https://github.com/jordansissel/fpm/archive/v${FPM_VERSION}.tar.gz" -o
fpm-${FPM_VERSION}.tar.gz \  
&& echo "${FPM_SHA256} fpm-${FPM_VERSION}.tar.gz" | sha256sum -c - \  
&& mkdir -p fpm \  
&& tar xf fpm-${FPM_VERSION}.tar.gz -C fpm --strip-components=1 \  
&& cd fpm \  
&& gem build fpm.gemspec \  
&& gem install --no-rdoc --no-ri fpm-${FPM_VERSION}.gem \  
&& cd .. \  
&& rm -rf fpm \  
&& rm fpm-${FPM_VERSION}.tar.gz  
  
CMD ["fpm"]  

