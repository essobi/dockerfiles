FROM huksley/ubuntu-dind  
MAINTAINER Innovative People <contact@inpglobal.com>  
  
# Let's start with some basic stuff.  
run apt-get update -q  
run apt-get install -y curl git maven tzdata  
run apt-get install -y python-pip openssh-client  
run pip install docker-compose  
  
ENV JAVA_TOOL_OPTIONS -Dfile.encoding=UTF-8  
RUN locale-gen en_US.UTF-8 && \  
localedef -i en_US -c -f UTF-8 en_US.UTF-8 && \  
ln -fs /usr/share/zoneinfo/Europe/Moscow /etc/localtime && \  
echo "Europe/Moscow" > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata && \  
sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
echo 'LANG="en_US.UTF-8"' > /etc/default/locale && \  
update-locale LANG="en_US.UTF-8" LANGUAGE="en_US" && \  
dpkg-reconfigure --frontend=noninteractive locales  
  

