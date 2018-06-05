FROM rijalati/alpine-zulu-jdk8:latest  
MAINTAINER rijalati@gmail.com  
  
RUN apk update --no-cache \  
&& apk add git tar mksh && git clone https://github.com/rijalati/oltpbench.git  
WORKDIR /oltpbench  
RUN git checkout driver-bump  
COPY my-templates/ /oltpbench/templates/  
COPY config-templates/ /oltpbench/config-templates/  
COPY start.sh /start.sh  
COPY bench-confgen.sh bench-confgen.sh  
COPY ntlmauth.dll /oltpbench/lib/  
COPY db2jcc4-get.sh db2jcc4-get.sh  
RUN chmod +x oltpbenchmark /start.sh ojdbc-get.sh  
RUN git checkout driver-bump && git fetch  
RUN mvn clean && mvn package -P fixerrors  
  
ENV DBFQDN='' DBUSER='' DBPASS='' DBTYPE='' DBNAME='' DBPORT='' BENCH='' \  
MVN_PASS='' CLEARBOOL='' CREATEBOOL='' EXECBOOL='' LOADBOOL='' SCALE='' \  
ORACLEMVN_USER='' ORACLEMVN_PASS='' BASICAUTH='' RATE='' CLIENTS='' \  
ISOLATION='' ACCEPT_OTN_BOOL=''  
ENTRYPOINT ["/start.sh"]  

