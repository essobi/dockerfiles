FROM python:3.6  
LABEL maintainer "Cheewai Lai <clai@csir.co.za>"  
  
ARG GOSU_VERSION=1.10  
ARG
GOSU_DOWNLOAD_URL="https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-
amd64"  
ARG DEBIAN_FRONTEND=noninteractive  
ARG DOCKERIZE_VERSION=v0.5.0  
  
RUN pip3 install asyncpg \  
&& pip3 install async-timeout \  
&& pip3 install chardet \  
&& pip3 install multidict \  
&& pip3 install yarl \  
&& pip3 install aiohttp \  
&& pip3 install aiopg \  
&& pip3 install aiodns \  
&& pip3 install aioamqp \  
&& pip3 install aiomysql \  
&& pip3 install aiofiles \  
&& pip3 install rethinkdb \  
&& pip3 install dateutils \  
&& pip3 install pytest \  
&& pip3 install numpy \  
&& pip3 install blinker raven raven_aiohttp --upgrade \  
&& apt-get update \  
&& apt-get -y install curl python3-shapely python3-jinja2 python3-yaml \  
&& curl -o gosu -fsSL "$GOSU_DOWNLOAD_URL" > gosu-amd64 \  
&& mv gosu /usr/bin/gosu \  
&& chmod +x /usr/bin/gosu \  
&& curl -k -fsSL
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz | tar xfz - -C /usr/bin \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod 755 /docker-entrypoint.sh \  
&& chown root.root /docker-entrypoint.sh  

