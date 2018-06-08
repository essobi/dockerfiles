FROM java:8  
RUN (apt-get update; apt-get install nano -y )  
RUN mkdir /portal  
WORKDIR /portal  
ADD portal.sh /portal/portal.sh  
RUN wget
https://dma.ci.cloudbees.com/job/MaritimeCloudPortal/lastBuild/artifact/target/maritimecloud-
portal-0.1.1.war -O /portal/maritimecloud-portal-0.1.1.war  
EXPOSE 8080  
#ENTRYPOINT ["/portal/portal.sh"]  
#CMD ["start"]  
ENTRYPOINT ["java", "-jar"]  
CMD ["maritimecloud-portal-0.1.1.war"]  

