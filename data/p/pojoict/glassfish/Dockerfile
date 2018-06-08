FROM pojoict/jdk:8.0  
MAINTAINER Pojo-ict  
  
RUN apt-get update > /dev/null && \  
apt-get install -y expect > /dev/null && \  
apt-get clean > /dev/null && \  
rm -rf /var/lib/apt/lists/* && \  
curl -Lks
http://dlc.sun.com.edgesuite.net/glassfish/4.1/release/glassfish-4.1.zip -o
glassfish.zip && \  
unzip -q /glassfish.zip && \  
rm -rf glassfish.zip && \  
mkdir /config  
  
ADD config/* /config/  
  
RUN echo '' >> /etc/profile \  
RUN echo '# GLASSFISH_HOME' >> /etc/profile \  
RUN echo "export GLASSFISH_HOME=/glassfish4/glassfish" >> /etc/profile \  
RUN echo 'export PATH=$PATH:GLASSFISH_HOME/bin' >> /etc/profile \  
RUN echo '' >> /etc/profile  
  
ENV GLASSFISH_HOME /glassfish4/glassfish  
ENV PATH /glassfish4/glassfish/bin:$PATH  
  
# 4848 (administration), 8080 (HTTP listener), 8181 (HTTPS listener), 9009
(DEBUG port)  
EXPOSE 4848 8080 8181 9009  
CMD cd /config && sh ./run.sh  

