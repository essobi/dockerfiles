FROM debian:latest  
MAINTAINER laurent NGAKO <laurent.ngako@gmail.com>  
  
#Intall curl  
RUN apt-get update -y  
# Install ca-certificates to support ssl connections.  
RUN apt-get install ca-certificates -y  
#Install curl  
RUN apt-get install curl -y  
#Install wget  
RUN apt-get install wget -y  
#Install git  
RUN apt-get install git -y  
#Install vim to edit the files.  
RUN apt-get install -y vim  
#Intall nodejs see: https://nodejs.org/en/download/package-manager/#debian-
and-ubuntu-based-linux-distributions  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
  
#expose port 3000 for test  
EXPOSE 3000  
#Create dev folder and use it.  
RUN mkdir /home/dev/  
  
#Go to working directory  
WORKDIR /home/dev/  
  
# Add gosu  
ENV GOSU_VERSION 1.9  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates && rm -rf /var/lib/apt/lists/* \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get purge -y --auto-remove ca-certificates  
  
# Copy file to create local user into container  
COPY ./add-local-user.sh /usr/local/bin/add-local-user  
RUN chmod +x /usr/local/bin/add-local-user  
  
# Add default developer user name  
ENV LOCAL_USER_NAME dev

