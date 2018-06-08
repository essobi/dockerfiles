# BUILD docker build -t crosbymichael/ajenti --rm=true .  
# RUN docker run -d --name ajenti -p 0.0.0.0:8000:8000 crosbymichael/ajenti  
# sudo ufw allow from 127.0.0.1 to any port 8001  
FROM crosbymichael/python  
  
RUN apt-get clean all; apt-get update; apt-get install -y wget  
RUN wget http://repo.ajenti.org/debian/key -O- | apt-key add -  
RUN echo "deb http://repo.ajenti.org/ng/debian main main ubuntu" >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y ajenti  
  
EXPOSE 8000  
ENTRYPOINT ["ajenti-panel"]  

