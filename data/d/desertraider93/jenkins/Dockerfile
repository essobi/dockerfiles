FROM ubuntu  
RUN apt update && apt install -y wget apt-transport-https openjdk-8-jre
icedtea-8-plugin curl  
RUN wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | apt-key add -  
RUN echo 'deb https://pkg.jenkins.io/debian binary/' >> /etc/apt/sources.list  
RUN apt update  
COPY startJenkins /  
RUN chmod +x /startJenkins  
RUN cd / && wget -q --content-disposition
http://mirrors.jenkins.io/war/latest/jenkins.war  
EXPOSE 8080  
CMD [ "/startJenkins", "start", "FOREGROUND" ]

