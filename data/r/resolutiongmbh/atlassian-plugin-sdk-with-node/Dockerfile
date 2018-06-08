FROM openjdk:8-jdk  
  
# Maintainers on this project are the following:  
MAINTAINER MAINTAINER Tobias Theobald <t.theobald@resolution.de>  
  
RUN apt-get update \  
&& apt-get install -y apt-transport-https  
  
# Install the Atlassian Plugins SDK using the official Aptitude debian  
# package repository  
RUN echo "deb https://sdkrepo.atlassian.com/debian/ stable contrib" >>
/etc/apt/sources.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
B07804338C015B73 \  
&& apt-get update \  
&& apt-get install -y atlassian-plugin-sdk  
  
# Copy Maven preference files to predefine the command line question about  
# subscribing to the mailing list to `NO`.  
COPY resources/.java /root/.java  
  
# Install Node.js for web development dependencies  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y nodejs  
  
# Create directory for sources using the same practice as the ruby images  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Set the default running command of the AMPS image to be running the  
# application in debug mode.  
CMD ["atlas-version"]  

