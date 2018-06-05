# Splunk  
#  
# 6.1.3  
#Start from ubuntu. This has to be first.  
FROM ubuntu  
  
ENV REFRESHED_AT 2014-08-29  
MAINTAINER Alex Munk <alexanderm@gmail.com>  
  
#update ubuntu  
#RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
#update apt-get  
RUN apt-get update  
  
#install wget  
RUN apt-get install -y wget  
  
#install splunk using .deb  
RUN wget -O /opt/splunk-6.1.3-220630-linux-2.6-amd64.deb
'http://www.splunk.com/page/download_track?file=6.1.3/splunk/linux/splunk-6.1.3-220630-linux-2.6-amd64.deb&ac=&wget=true&name=wget&platform=Linux&architecture=x86_64&version=6.1.3&product=splunk&typed=release'  
RUN dpkg -i /opt/splunk-6.1.3-220630-linux-2.6-amd64.deb  
  
#create the splunk service as root  
RUN /opt/splunk/bin/splunk enable boot-start --accept-license  
RUN chmod 755 /etc/init.d/splunk #give read/execute to non-root users (like
splunk user)  
RUN chown -R splunk:splunk /opt/splunk #enable boot-start creates a bunch of
stuff as root, so re-chown the whole splunk dir to splunk:splunk  
  
USER splunk  
  
  
EXPOSE 8000  
EXPOSE 8089  
EXPOSE 9997  
#/opt/splunk/bin/splunk start starts both splunkweb and splunkd in the
background. Then /opt/splunk/bin/splunk start exits, and when it does, docker
thinks the container should stop. Containers are designed to run one process,
in the foreground.  
#note: could run splunkweb and splunkd in separate containers. challenge is
that distributed splunk is hard (app installation, config, etc.)  
#note: running any process in the background will get kill -9'ed when the
container is stopped (meaning the process won't be shut down gracefully)  
#note: running splunkweb in the background and splunkd in the foreground will
mostly work, but will have the limitation that if a license is changed and
splunkd is killed, there will be nothing to restart it (this is the problem
that amrit brought up)  
#CMD ["start", "splunkd", "--nodaemon"]  
#ENTRYPOINT ["/opt/splunk/bin/splunk"]  
#The following CMD and ENTRYPOINT succeed at running the command
"/opt/splunk/bin/splunk start --answer-yes" when a container is run, but it
still doesn't leave splunk running. I still have to ^p^q or the process stops.  
#CMD ["start", "--answer-yes"]  
#ENTRYPOINT ["/opt/splunk/bin/splunk"]  
#To start splunk using this image, one has to run -i (interactive) and service
splunk start from the prompt, and then exit with ^p^q to keep the container
running. I guess better would be to sudo docker run -d -P alexanderm/splunk:v1
service splunk start, so at least the first thing the container does is start
splunk, but for some reason that dies.  

