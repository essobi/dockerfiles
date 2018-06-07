FROM mono  
LABEL maintainer "Sylvain VISTE <viste.sylvain@gmail.com>"  
RUN apt-get update && \  
apt-get install -y wget unzip && \  
wget "https://s3-us-west-2.amazonaws.com/eco-
releases/EcoServer_v0.7.2.1-beta.zip" -O /tmp/EcoServer.zip && \  
unzip /tmp/EcoServer.zip -d /app/ && \  
rm /tmp/EcoServer.zip  
EXPOSE 2999/udp 3000 3001  
WORKDIR /app  
CMD ["mono", "EcoServer.exe", "-nogui"]  

