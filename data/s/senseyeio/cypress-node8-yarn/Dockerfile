FROM ubuntu:xenial  
  
RUN apt-get update \  
&& apt-get install -y apt-transport-https curl  
  
# Install Node 8.x  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get update \  
&& apt-get install -y nodejs  
  
# Install yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
# Install Git client  
RUN apt-get update  
  
# Do installs  
RUN apt-get install -y git yarn  
  
RUN git --version  
  
# Install Cypress dependencies (separate commands to avoid time outs)  
RUN apt-get install -y \  
libgtk2.0-0  
RUN apt-get install -y \  
libnotify-dev  
RUN apt-get install -y \  
libgconf-2-4 \  
libnss3 \  
libxss1  
RUN apt-get install -y \  
libasound2 \  
xvfb  
  
# Install Cypress and Typescript  
#RUN yarn global add cypress typescript  
#RUN cypress verify  
CMD ["/bin/bash"]  

