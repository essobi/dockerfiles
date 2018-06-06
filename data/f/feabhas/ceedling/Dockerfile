FROM gcc:latest  
  
ENV REFRESHED_AT 2018-02-01  
# Set up a tools dev dierctory  
WORKDIR /home/dev  
  
RUN apt-get -qq update \  
&& apt-get -y install git bzr lib32z1 lib32ncurses5 ruby-full python-pip \  
&& gem install ceedling \  
&& pip install --upgrade pip \  
&& pip install --upgrade virtualenv \  
&& pip install gcovr  
  
WORKDIR /usr/project  
  

