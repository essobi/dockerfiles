FROM debian  
MAINTAINER Max D <lugamax@gmail.com>  
  
ADD init.sh /init.sh  
RUN apt-get update \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get install -q -y mysql-server \  
&& chmod 777 /init.sh  

