# Copyright 2016 Jiglesgom  
FROM jiglesgom/mvn  
LABEL maintainer "jiglesgom@gmail.com"  
  
#clonar Netflix from github https://github.com/Tschuss/Netflix.git  
RUN env GIT_SSL_NO_VERIFY=true git clone
https://github.com/Tschuss/Netflix.git  
  
WORKDIR /Netflix/Springboot_hystrix-dashboard  
RUN env GIT_SSL_NO_VERIFY=true git pull  
RUN mvn install  
  
# Standard Hystrix dashboard port  
EXPOSE 7979  
CMD ["/usr/lib/jvm/java-8-oracle/bin/java", "-jar",
"/Netflix/Springboot_hystrix-
dashboard/target/HystrixDashboardApplication-0.0.1-SNAPSHOT.jar", "-Xmx128M"]

