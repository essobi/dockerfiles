FROM microsoft/aspnetcore-build  
MAINTAINER Certaincy  
  
# This is for mono. Thanks a lot, CAKE...  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
RUN echo "deb http://download.mono-project.com/repo/debian jessie main" | tee
/etc/apt/sources.list.d/mono-official.list  
RUN apt-get update  
RUN apt install mono-complete wget -y  
  
# Install Heroku CLI  
RUN wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh  

