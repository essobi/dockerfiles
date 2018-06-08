FROM openjdk:8-jre-alpine  
  
ADD https://github.com/evsinev/mysql-scheduler/releases/download/mysql-
scheduler-1.0-9/scheduler-1.0-10-SNAPSHOT.jar /scheduler.jar  
  
ENV URL
"jdbc:mysql://mysql:3306/sched?logger=Slf4JLogger&noAccessToProcedureBodies=true&useInformationSchema=true&autoReconnect=false&characterEncoding=utf8"  
CMD ["/usr/bin/java", "-jar", "/scheduler.jar"]  

