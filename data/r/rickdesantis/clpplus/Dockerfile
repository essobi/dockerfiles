FROM alpine:latest  
MAINTAINER Riccardo B. Desantis <riccardobenito.desantis@gmail.com>  
  
# Setting the environment  
ENV HOSTNAME clpplus.rickdesantis.docker.com  
ENV USERHOME /root  
ENV USER root  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
ENV PATH $USERHOME/dsdriver/bin:$JAVA_HOME/bin:$PATH  
ENV DB_HOSTNAME host  
ENV DB_USER user  
ENV DB_PASSWORD password  
ENV DB_PORT 50000  
ENV DB_NAME BLUDB  
  
WORKDIR $USERHOME  
# Update the repos and install all the used packages  
RUN apk update && apk add --no-cache \  
mksh \  
libxml2 \  
unzip \  
openjdk8-jre-base  
  
# Install the client  
ADD ibm_data_server_driver_package_linuxx64_v10.5.tar.gz .  
WORKDIR $USERHOME/dsdriver  
RUN sed 's|/bin/ksh|/bin/mksh|' < installDSDriver > installDSDriver-new && \  
mv installDSDriver-new installDSDriver && \  
chmod +x installDSDriver && \  
./installDSDriver  
WORKDIR $USERHOME/dsdriver/bin  
RUN mv clpplus clpplus-orig && \  
printf "%b\n" '#!'"`which env` sh\n\ncd $USERHOME/dsdriver/bin\nif [ \$# -eq 0
]; then\nsh ../db2profile && exec clpplus-orig -nw
\$DB_USER/\$DB_PASSWORD@\$DB_HOSTNAME:\$DB_PORT/\$DB_NAME\nelse\nsh
../db2profile && exec clpplus-orig -nw \"\$@\"\nfi" > clpplus && \  
chmod +x clpplus  
  
ENTRYPOINT [ "clpplus" ]  
  
# Build: docker build -t clpplus1 ../clpplus  
# Run: docker run --name=clpplus1 -it clpplus1 <user>/<password>@<host>:<port
| 50000>/<dbname | BLUDB>  
# Bash: docker exec -it clpplus1 bash  
# Start: docker start clpplus1  
# Stop: docker stop clpplus1  

