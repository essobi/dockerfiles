FROM schickling/beanstalkd-console  
MAINTAINER Christopher Willard "cwillard@carqualifier.com"  
RUN apt-get update \  
&& apt-get install -y wget \  
&& wget
https://github.com/src-d/beanstool/releases/download/v0.2.0/beanstool_v0.2.0_linux_amd64.tar.gz
\  
&& tar -xvzf beanstool_v0.2.0_linux_amd64.tar.gz \  
&& cp -R beanstool_v0.2.0_linux_amd64/beanstool /usr/local/bin/  

