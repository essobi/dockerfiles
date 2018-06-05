FROM python:3.5.2  
# TODO replace by a light-weight image like alpine  
MAINTAINER Jesús Pardillo "dev@jesuspardillo.com"  
########### from https://denibertovic.com/posts/handling-permissions-with-
docker-volumes  
RUN apt-get update && apt-get -y --no-install-recommends install \  
ca-certificates \  
curl  
  
ENV GOSU_VERSION 1.10  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
  
###########  
RUN pip install --upgrade bumpversion  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh", "/usr/local/bin/bumpversion"]  

