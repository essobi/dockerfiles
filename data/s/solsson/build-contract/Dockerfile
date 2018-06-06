FROM
yolean/node@sha256:9f4a2b32e4ba065ea5471d4d83084d4ba1f860a8bde614518b386999bf0cf9b2  
  
ENV docker_version=17.09.1~ce-0~debian  
ENV compose_version=1.21.0
compose_sha256=af639f5e9ca229442c8738135b5015450d56e2c1ae07c0aaa93b7da9fe09c2b0  
  
RUN apt-get update \  
&& apt-get install -y apt-transport-https curl ca-certificates gnupg2 \  
&& curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - \  
&& apt-key fingerprint 0EBFCD88 \  
&& echo "deb [arch=amd64] https://download.docker.com/linux/debian stretch
stable" > /etc/apt/sources.list.d/docker.list \  
&& apt-get update \  
&& apt-get install -y docker-ce=$docker_version \  
&& rm -r /var/lib/apt/lists/*  
  
# This image expects a mounted docker.sock or env that points to docker tcp  
RUN update-rc.d -f docker remove  
  
RUN curl -L
https://github.com/docker/compose/releases/download/$compose_version/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \  
&& sha256sum /usr/local/bin/docker-compose \  
&& echo "${compose_sha256} /usr/local/bin/docker-compose" | sha256sum -c - \  
&& chmod +x /usr/local/bin/docker-compose  
  
VOLUME /source  
WORKDIR /source  
  
COPY package.json /usr/src/app/  
RUN cd /usr/src/app/ && npm install --production  
COPY build-contract parsetargets /usr/src/app/  
COPY nodejs /usr/src/app/nodejs  
RUN cd /usr/src/app/ && npm link --only=production  
  
ENTRYPOINT ["build-contract"]  
CMD ["push"]  

