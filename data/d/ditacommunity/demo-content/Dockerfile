FROM java:8  
MAINTAINER Eliot Kimber "ekimber@contrext.com"  
# Defines a data volume container for the DITA Demo  
# Content collection ("Thunderbird").  
#  
RUN mkdir -p /opt/dita-community/data  
WORKDIR /opt/dita-community/data  
# Get the Thunderbird directory from github then make just  
# the Thunderbird directory into a new git repo for use  
# with the DFST system in isolation, no relation to the  
# github repo.  
RUN git clone http://github.com/dita-community/dita-demo-content-
collection.git && \  
cd dita-demo-content-collection && \  
git checkout dita-1.3 && \  
mv Thunderbird .. && \  
cd .. && \  
rm -Rf dita-demo-content-collection  
WORKDIR /opt/dita-community/data/Thunderbird  
# NOTE: We need the email and user settings in order for  
# the commit to succeed.  
RUN git init && \  
git config --global user.email "thunderbird@dita-community.org" && \  
git config --global user.name "Thunderbird" &&\  
git add -A && \  
git commit -m "Initial setup"  
VOLUME /opt/dita-community/data/Thunderbird  
#  
# End of Dockerfile  
#  

