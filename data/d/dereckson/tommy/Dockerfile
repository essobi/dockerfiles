#  
# Tommy Docker image  
# A simple Hudson/Jenkins dashboard view  
#  
FROM ruby:2.2  
MAINTAINER Sébastien Santoro aka Dereckson <dereckson+nasqueron-docker@espace-
win.org>  
  
#  
# Prepare the container  
#  
ENV LANG C.UTF-8  
RUN mkdir -p /usr/src/app && \  
git clone https://github.com/nasqueron/tommy.git /usr/src/app && \  
cd /usr/src/app && \  
bundle install  
  
#  
# Run the container  
#  
EXPOSE 4567  
WORKDIR /usr/src/app  
CMD ["ruby", "/usr/src/app/tommy.rb", "-o", "0.0.0.0"]  

