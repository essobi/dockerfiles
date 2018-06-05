FROM calfater/base-image:latest  
  
RUN apt-get update \  
&& apt-get install -y software-properties-common python-software-properties
sudo  
  
RUN add-apt-repository ppa:seafile/seafile-client \  
&& apt-get update \  
&& apt-get install -y seafile-cli  
  
ENV UID=1000  
ENV GID=1000  
ENTRYPOINT ["/home/seafile/start.sh"]  
  
VOLUME ["/home/seafile/config" "/home/seafile/libraries"]  
  
COPY ["start.sh", "/home/seafile/"]  
COPY ["script.sh", "/home/seafile/"]  
RUN ["chmod", "+x", "/home/seafile/start.sh", "/home/seafile/script.sh"]  
  

