# Ubuntu 15.10 with Java 8 installed and Datenverteiler 3.6.4.  
# Build image with: docker build -t christian/datenverteiler:3.6.4 .  
FROM ubuntu:15.10  
MAINTAINER Christian Hösel, https://github.com/christianhoesel  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y software-properties-common && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections &&\  
apt-get install -y oracle-java8-installer && \  
apt-get clean  
COPY Kernsoftware-Basissystem Kernsoftware-Basissystem  
#ENTRYPOINT ["bash","Kernsoftware-Basissystem/skripte-
bash/KernsoftwareSystem.sh"]  
EXPOSE 8083  
EXPOSE 2323  
#CMD ["bash","Kernsoftware-Basissystem/skripte-bash/KernsoftwareSystem.sh"]  
CMD ["bash","Kernsoftware-Basissystem/skripte-bash/StartStopp.sh"]  

