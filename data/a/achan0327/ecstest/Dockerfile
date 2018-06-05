FROM ubuntu:14.04  
# make sure apt is up to date  
RUN apt-get update  
RUN apt-get -y -qq install python wget git git-core  
  
# install nodejs and npm  
RUN \  
wget -O - http://nodejs.org/dist/v0.10.29/node-v0.10.29-linux-x64.tar.gz \  
| tar xzf - --strip-components=1 --exclude="README.md" \--exclude="LICENSE" \  
\--exclude="ChangeLog" -C "/usr/local"  
  
# Set the working directory  
RUN git clone
https://d198f67e87a9110862c01291706758c8f919ffd6:x-oauth@github.com/antonychan/ecs-
test src  
  
# Set the working directory to where we just cloned to  
WORKDIR /src  
  
RUN npm i  
  
EXPOSE 80  
CMD ["/bin/bash"]  

