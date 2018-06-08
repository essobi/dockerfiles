FROM alpine:latest  
MAINTAINER Hleb Rubanau <g.rubanau@gmail.com>  
  
ARG confd_version=0.14.0  
RUN apk add --update wget curl ca-certificates \  
&& wget -q -O /usr/local/bin/confd
https://github.com/kelseyhightower/confd/releases/download/v${confd_version}/confd-${confd_version}-linux-
amd64 \  
&& chmod +x /usr/local/bin/confd \  
&& mkdir -p /etc/confd  
  
# prebuilt compose is not compatible with alpine -- copycatting  
# https://github.com/tjamet-docker/docker-compose/blob/master/Dockerfile  
ARG compose_version=1.18.0  
RUN apk --no-cache add python py-pip git &&\  
git clone --branch ${compose_version} https://github.com/docker/compose.git
/code/compose &&\  
cd /code/compose &&\  
pip --no-cache-dir install -r requirements.txt -r requirements-dev.txt
pyinstaller==3.1.1 &&\  
git rev-parse --short HEAD > compose/GITSHA &&\  
ln -s /lib /lib64 && ln -s /lib/libc.musl-x86_64.so.1 ldd && ln -s /lib/ld-
musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 && \  
pyinstaller docker-compose.spec &&\  
unlink /lib/ld-linux-x86-64.so.2 /lib64 ldd ||true &&\  
mv dist/docker-compose /usr/local/bin/docker-compose &&\  
pip freeze | xargs pip uninstall -y &&\  
apk del python py-pip git &&\  
rm -rf /code /usr/lib/python2.7/ /root/.cache /var/cache/apk/* &&\  
chmod +x /usr/local/bin/docker-compose  
  
# not sure what is in the alpine package -- we only need docker cli  
ARG DOCKER_CLI_VERSION=17.03.2  
RUN wget -q -O /tmp/docker.tgz \  
https://download.docker.com/linux/static/stable/$(uname
-m)/docker-${DOCKER_CLI_VERSION}-ce.tgz \  
&& cd /tmp \  
&& tar -xzf docker.tgz \  
&& cp docker/docker /usr/local/bin/docker \  
&& rm -rf /tmp/docker*  
  
COPY docker-sigkill.sh /usr/local/bin/docker-sigkill  
RUN chmod a+x /usr/local/bin/docker-sigkill  
  
ENTRYPOINT ["confd"]  

