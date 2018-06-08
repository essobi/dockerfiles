FROM ubuntu:xenial  
MAINTAINER Chris Johns <chris@ter0.net> @ter0  
  
ARG user=mumble  
ARG group=mumble  
ARG uid=1000  
ARG gid=1000  
ARG home=/home/${user}/  
  
RUN groupadd --gid ${gid} ${group} \  
&& useradd --create-home --home ${home} \--uid ${uid} \--gid ${gid} ${user} \  
&& echo "deb http://ppa.launchpad.net/mumble/release/ubuntu xenial main" >>
/etc/apt/sources.list.d/mumble.list \  
&& echo "deb-src http://ppa.launchpad.net/mumble/release/ubuntu xenial main"
>> /etc/apt/sources.list.d/mumble.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 85DECED27F05CF9E \  
&& apt-get update \  
&& apt-get install -y mumble-server=1.2.16-1~ppa1~xenial1  
  
VOLUME ${home}  
  
COPY mumble-server.ini ${home}/mumble-server.ini  
  
RUN chown -R ${user}:${group} ${home}  
  
EXPOSE 64738/udp  
  
USER ${user}  
  
WORKDIR ${home}  
  
ENTRYPOINT ["/usr/sbin/murmurd", "-fg", "-ini", "mumble-server.ini"]  

