FROM centos:7  
MAINTAINER nalinda@thinkcube.com  
  
RUN yum install -y https://rpm.nodesource.com/pub_4.x/el/7/x86_64/nodesource-
release-el7-1.noarch.rpm  
RUN yum install -y nodejs vim gcc-c++ make git bzip2 && yum clean all  
  
RUN npm install -g npm  
  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys BF357DD4 \  
&& curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.9/gosu-amd64" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.9/gosu-amd64.asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod 4755 /usr/local/bin/gosu  
  
RUN useradd --shell /bin/bash -u 1000 -o -c "" -m user \  
&& usermod -aG root user  
  
RUN sed -i "1ialias ls='ls --color'" /home/user/.bashrc \  
&& sed -i "2ialias yum='gosu root yum'" /home/user/.bashrc  
  
WORKDIR /opt  
VOLUME ["/opt"]  
CMD ["npm", "start"]  
  

