FROM java:8-jdk  
  
ENV ACTIVATOR_VERSION 1.3.12  
RUN apt-get update && \  
apt-get install -y git build-essential curl wget zip unzip software-
properties-common  
  
# Install play  
RUN wget http://downloads.typesafe.com/typesafe-
activator/${ACTIVATOR_VERSION}/typesafe-activator-${ACTIVATOR_VERSION}.zip &&
\  
unzip typesafe-activator-${ACTIVATOR_VERSION}.zip && \  
mv activator-dist-${ACTIVATOR_VERSION} /opt/activator && \  
chmod 777 -R /opt/activator && \  
rm typesafe-activator-${ACTIVATOR_VERSION}.zip  
  
RUN mkdir -p /src  
WORKDIR /src  
  
#so activator will put cache file in /var/home  
ENV _JAVA_OPTIONS='-Duser.home=/var/home'  
env PATH /opt/activator/bin/:$PATH  
  
EXPOSE 9000  

