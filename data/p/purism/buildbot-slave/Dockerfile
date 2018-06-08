FROM jpetazzo/dind  
  
MAINTAINER Ryan Smith-Roberts <rmsr@puri.sm>  
  
ENV GOSU_VERSION 1.3  
# grab gosu for easy step-down from root  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN apt-get -q update \  
&& apt-get install -yq curl \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/* \  
&& curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& apt-get purge -y --auto-remove curl  
  
RUN apt-get -q update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -qy \  
python-pip python-dev git sudo \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
RUN pip install buildbot-slave  
  
RUN groupadd -r buildbot \  
&& useradd -r -d /slave -g buildbot -G docker buildbot \  
&& mkdir /slave  
  
COPY ./run.sh /  
CMD ["wrapdocker", "/run.sh"]  

