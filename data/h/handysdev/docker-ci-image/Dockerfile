FROM python:3.6-stretch  
MAINTAINER Dongeon Kim <dongeon.kim@handys.co.kr>  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install build-essential postgresql-client -y \  
&& pip install awscli \  
&& curl -sL https://deb.nodesource.com/setup_9.x | bash - \  
&& apt-get install nodejs -y  
  
WORKDIR /root  
ADD entrypoint.sh /root/entrypoint.sh  
RUN chmod +x entrypoint.sh  
CMD ["sh", "entrypoint.sh"]  

