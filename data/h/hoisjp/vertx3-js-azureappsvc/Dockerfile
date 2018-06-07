# Extend vert.x image (1)  
FROM vertx/vertx3  
  
# Azure Web App: SSH Server support  
# see also https://docs.microsoft.com/en-us/azure/app-service/containers/app-
service-linux-ssh-support#ssh-support-with-custom-docker-images  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends openssh-server \  
&& echo "root:Docker!" | chpasswd  
  
COPY sshd_config /etc/ssh/  
  
# Set the name of the verticle to deploy (2)  
ENV VERTICLE_NAME hello-verticle.js  
  
# Set the location of the verticles (3)  
ENV VERTICLE_HOME /usr/verticles  
  
# Azure Web App: Adding 2222 port  
EXPOSE 8080 2222  
# Copy your verticle to the container (4)  
COPY $VERTICLE_NAME $VERTICLE_HOME/  
  
# Launch the verticle (5)  
WORKDIR $VERTICLE_HOME  
  
# Azure Web App: Launch ssh service and verticle  
#ENTRYPOINT ["sh", "-c"]  
#CMD ["exec vertx run $VERTICLE_NAME -cp $VERTICLE_HOME/*"]  
COPY start.sh .  
RUN chmod 755 ./start.sh  
ENTRYPOINT ["./start.sh"]  

