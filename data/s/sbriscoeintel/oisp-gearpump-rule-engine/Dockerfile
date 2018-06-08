FROM ubuntu  
  
RUN apt-get update && apt-get install curl default-jre unzip python-setuptools
-y  
  
WORKDIR /gearpump  
  
RUN curl --location --retry 3 --insecure
https://github.com/gearpump/gearpump/releases/download/0.8.0/gearpump-2.11-0.8.0.zip
-o tmp.zip && unzip -q tmp.zip && rm tmp.zip && chmod +x
gearpump-2.11-0.8.0/bin/*  
  
ADD gear.conf gearpump-2.11-0.8.0/conf/gear.conf  
  
EXPOSE 8090  
WORKDIR /app  
COPY deployer/src /app/deployer/src  
ADD wait-for-it.sh .  
  
RUN easy_install poster  
RUN easy_install requests  
  
RUN apt-get install software-properties-common -y && \  
add-apt-repository ppa:deadsnakes/ppa && \  
apt-get update && \  
apt-get install -y python2.7  
  
COPY \--from=sbriscoeintel/oisp-gearpump-rule-engine /app/app.jar /app/app.jar  
  
ENV RULE_ENGINE_PACKAGE_NAME /app/app.jar  
WORKDIR /app/deployer/src  
  
ADD scripts/bootstrap.sh scripts/bootstrap.sh  
  
ENTRYPOINT ["scripts/bootstrap.sh"]  

