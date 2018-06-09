# Based on default python image  
FROM python:3.5-slim  
  
# Force the binary layer of the stdout and stderr streams to be unbuffered.  
ENV PYTHONUNBUFFERED 1  
# Upgrade packages if necessary  
RUN apt-get update && apt-get upgrade -y  
  
RUN apt-get install -y curl && curl -sL https://deb.nodesource.com/setup_4.x |
bash -  
  
# Install required packages and delete cache  
RUN apt-get install -y --no-install-recommends apt-utils mysql-client \  
libmysqlclient-dev ruby-dev ruby-ffi ruby nodejs git cron redis-tools \  
gcc g++ gettext libcurl4-openssl-dev libssl-dev \  
vim nano mc curl  
  
# Install required tools  
RUN gem install sass scss_lint  
RUN npm install jscs -g  
  
# The app will be located here  
ENV WORKDIR /app  
RUN mkdir -p $WORKDIR && mkdir -p /var/log/statusdroid/  
WORKDIR $WORKDIR  
  
# Add requirements.txt file to docker image  
ADD ./requirements.txt $WORKDIR  
  
# Upgrade pip and install dependencies  
RUN LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "pip3 install --upgrade pip && pip3
install -r requirements.txt && rm ./requirements.txt"  
  
# Set LOCATION,REGION,SERVER_GUID to global ENV  
RUN echo 'export LOCATION=$(curl --retry 2 --connect-timeout 1 -s
http://169.254.169.250/2016-07-29/self/host/labels/LOCATION)' >> /etc/profile
&& \  
echo 'export REGION=$(curl --retry 2 --connect-timeout 1 -s
http://169.254.169.250/2016-07-29/self/host/labels/REGION)' >> /etc/profile &&
\  
echo 'export SERVER_GUID=$(curl --retry 2 --connect-timeout 1 -s
http://169.254.169.250/2016-07-29/self/host/labels/SERVER_GUID)' >>
/etc/profile  
  
# Set UTC timezone for our servers  
RUN rm /etc/localtime && ln -s /usr/share/zoneinfo/UTC /etc/localtime && date  

