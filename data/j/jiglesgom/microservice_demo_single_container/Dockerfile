# Copyright 2016 Jiglesgom  
FROM jiglesgom/mvn  
MAINTAINER jiglesgom <jiglesgom@gmail.com>  
  
#clonar Netflix from github https://github.com/Tschuss/Netflix.git  
RUN env GIT_SSL_NO_VERIFY=true git clone -b single_container
https://github.com/Tschuss/Netflix.git && \  
cd /Netflix/Springboot_eureka; mvn install && \  
cd /Netflix/Springboot_zuul; mvn install && \  
cd /Netflix/Springboot_hystrix-dashboard; mvn install && \  
cd /Netflix/Springboot_hello; mvn install  
  
ADD start.sh /  
RUN chmod 755 /start.sh  
  
# Standard SSH port  
EXPOSE 8761 8762 8765 7979  
CMD ["/bin/bash", "/start.sh"]

