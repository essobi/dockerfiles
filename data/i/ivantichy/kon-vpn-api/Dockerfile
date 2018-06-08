FROM ivantichy/oracle-java8  
  
RUN apt-get update -y -q && \  
apt-get install openvpn -y -q && \  
apt-get install fail2ban -y -q && \  
apt-get install git -y -q && \  
apt-get install sudo -y -q && \  
rm -rf /var/lib/apt/lists/*  
  
# TODO add user  
RUN mkdir -p /home/java/ && cd /home/java/ && git clone \--branch master
https://github.com/ivantichy/koncentrator-backend-docker.git /home/java/  
  
WORKDIR /home/java  
  
RUN chmod +x ./Koncentrator/test/BasicTests/cleanserver.sh  
  
#RUN ./Koncentrator/test/BasicTests/cleanserver.sh  
COPY ./entrypoint.sh ./entrypoint.sh  
  
RUN chmod +x ./entrypoint.sh  
  
EXPOSE 10002  
ENTRYPOINT ["./entrypoint.sh"]  

