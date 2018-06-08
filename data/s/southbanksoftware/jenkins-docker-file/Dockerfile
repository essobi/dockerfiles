FROM ubuntu  
LABEL maintainer="developer@southbanksoftware.com"  
  
RUN sed -i -e 's/us.archive.ubuntu.com/archive.ubuntu.com/g'
/etc/apt/sources.list && apt-get update && apt-get install -y curl  
  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
openssh-client openssh-server rsync vim \  
dh-autoreconf libcurl4-gnutls-dev libexpat1-dev gettext libz-dev libssl-dev \  
&& curl -OL https://github.com/git/git/archive/v2.13.1.tar.gz \  
&& tar -zxf v2.13.1.tar.gz && cd git-2.13.1 && make configure && ./configure
--prefix=/usr && make all && make install && cd .. \  
&& apt-get remove -y dh-autoreconf libcurl4-gnutls-dev libexpat1-dev gettext
libz-dev libssl-dev \  
&& rm -rf v2.13.1.tar.gz git-2.13.1 \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo "unsafe-perm = true" > /root/.npmrc \  
&& echo "Australia/Melbourne" > /etc/timezone  
# && dpkg-reconfigure -f noninteractive tzdata  
  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - && apt-get install
-y nodejs && npm install -g yarn  
  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
build-essential \  
python \  
python-pip python-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& yarn global add node-gyp && pip install --upgrade pip && pip install
setuptools  
  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
openssh-client openssh-server rsync vim \  
dh-autoreconf libcurl4-gnutls-dev libexpat1-dev gettext libz-dev libssl-dev \  
&& curl -OL https://github.com/git/git/archive/v2.13.1.tar.gz \  
&& tar -zxf v2.13.1.tar.gz && cd git-2.13.1 && make configure && ./configure
--prefix=/usr && make all && make install && cd .. \  
&& apt-get remove -y dh-autoreconf libcurl4-gnutls-dev libexpat1-dev gettext
libz-dev libssl-dev \  
&& rm -rf v2.13.1.tar.gz git-2.13.1 \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo "unsafe-perm = true" > /root/.npmrc \  
&& echo "Australia/Melbourne" > /etc/timezone  
  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
build-essential \  
python \  
wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& yarn global add node-gyp  
  
RUN wget https://fastdl.mongodb.org/linux/mongodb-
linux-x86_64-debian71-3.2.13.tgz \  
&& tar -xzvf mongodb-linux-x86_64-debian71-3.2.13.tgz \  
&& echo 'export LC_ALL=C' >> /etc/default/locale  
  
RUN apt-get update \  
&& apt-get install -y python-pip python-dev \  
&& pip install mtools pymongo numpy \  
&& ln -sf /mongodb-linux-x86_64-debian71-3.2.13/bin/mongod /usr/bin/mongod \  
&& ln -sf /mongodb-linux-x86_64-debian71-3.2.13/bin/mongo /usr/bin/mongo \  
&& rm -rf /var/lib/apt/lists/*  
USER root  
RUN adduser jenkins  
RUN chmod 777 /home/jenkins  
ADD ./.aws /home/jenkins/.aws  
USER jenkins  

