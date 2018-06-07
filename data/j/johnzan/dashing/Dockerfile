# Dockerfile for dashing  
# http://shopify.github.io/dashing/#overview  
FROM ahromis/ruby  
  
MAINTAINER John Zanchetta <johnzan@gmail.com>  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# Prep for node install  
Run apt-get install g++ curl libssl-dev apache2-utils -y  
RUN apt-get install git-core -y  
  
# Install Node  
RUN git clone git://github.com/ry/node.git  
RUN cd node;./configure;make;sudo make install  
  
# Install Dashing  
RUN gem install dashing  
  
# Create a default dashboard  
RUN dashing new mydashboard  
RUN cd mydashboard;bundle  
  
# Launch the dashboard  
CMD cd /mydashboard;dashing start  

