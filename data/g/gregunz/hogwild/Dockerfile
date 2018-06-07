FROM openjdk:jre-alpine  
ADD opt /opt  
WORKDIR /opt/docker/bin  
RUN ["chmod", "+x", "hogwild"]  
RUN ["chmod", "+x", "start_node.sh"]  
RUN apk --no-cache add curl  
RUN apk --no-cache add ca-certificates  
ENTRYPOINT ["sh" , "start_node.sh"]  
CMD []  

