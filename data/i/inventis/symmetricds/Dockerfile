FROM openjdk:7-jre-jessie  
  
LABEL maintainer="Jan Esser <jane@inventis.be>"  
  
RUN apt-get update && apt-get -y install curl unzip  
  
RUN curl -L /opt
https://sourceforge.net/projects/symmetricds/files/symmetricds/symmetricds-3.8/symmetric-
server-3.8.35.zip > /opt/symmetricds.zip && \  
unzip /opt/symmetricds.zip -d /opt && \  
mv /opt/symmetric-server-3.8.35 /opt/symmetricds && \  
rm /opt/symmetricds.zip  
  
# Enable appropriate locales  
RUN apt-get update && apt-get install -y \  
locales  
  
RUN echo 'de_DE ISO-8859-1\n \  
de_DE.UTF-8 UTF-8\n \  
de_DE@euro ISO-8859-15\n \  
en_GB ISO-8859-1\n \  
en_GB.ISO-8859-15 ISO-8859-15\n \  
en_US ISO-8859-1\n \  
en_US.ISO-8859-15 ISO-8859-15\n \  
en_US.UTF-8 UTF-8\n \  
fr_FR ISO-8859-1\n \  
fr_FR.UTF-8 UTF-8\n \  
fr_FR@euro ISO-8859-15\n \  
nl_BE ISO-8859-1\n \  
nl_BE.UTF-8 UTF-8\n \  
nl_BE@euro ISO-8859-15\n \  
nl_NL ISO-8859-1\n \  
nl_NL.UTF-8 UTF-8\n \  
nl_NL@euro ISO-8859-15\n' \  
>> /etc/locale.gen && \  
/usr/sbin/locale-gen  
  
# Update timezone  
RUN echo 'Europe/Brussels' > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata  
  
  
COPY entrypoint.sh /entrypoint.sh  
  
RUN chmod +x /entrypoint.sh  
  
WORKDIR /opt/symmetricds  
  
ENTRYPOINT ["/entrypoint.sh"]  

