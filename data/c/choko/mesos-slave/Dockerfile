FROM choko/mesos  
  
# Let's start with some basic stuff.  
RUN apt-get update -qq && apt-get install -qqy \  
apt-transport-https \  
ca-certificates \  
lxc \  
iptables  
  
# Install Docker from Docker Inc. repositories.  
RUN echo deb https://get.docker.io/ubuntu docker main >
/etc/apt/sources.list.d/docker.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
36A1D7869245C8950F966E92D8576A8BA88D21E9 \  
&& apt-get update -qq \  
&& apt-get install -qqy lxc-docker  
  
# Install the magic wrapper.  
ADD ./run.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/run.sh  
  
# Define additional metadata for our image.  
VOLUME /var/lib/docker  
  
EXPOSE 5051  
CMD run.sh  

