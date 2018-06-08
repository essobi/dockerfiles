# Run like this:  
# sudo docker run -t -i --rm -p 8080:8080 <image-id>  
#  
# at deployment time the spring boot configuration properties are overridden
by environment variable provided by the AWS docker service, check  
# https://docs.spring.io/spring-boot/docs/current/reference/html/boot-
features-external-config.html for more information on spring boot
configuration  
#  
FROM java:8  
RUN wget
"https://dma.ci.cloudbees.com/job/NoGoService/lastSuccessfulBuild/artifact/nogo/build/libs/nogo.war"  
RUN wget
"https://dma.ci.cloudbees.com/job/NoGoService/lastSuccessfulBuild/artifact/dmiweather/build/libs/dmiweather.war"  
  
copy content/*.* ./  
RUN chmod a+x *.sh  
  
EXPOSE 8080  
# application prints directly to stdout, so we can forward it to CloudWatch
directly from the Container service

