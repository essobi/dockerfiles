FROM ubuntu:xenial  
MAINTAINER Kyle Manna <kyle@kylemanna.com>  
  
ARG USER_ID  
ARG GROUP_ID  
  
ENV HOME /monero  
  
# add user with specified (or default) user/group ids  
ENV USER_ID ${USER_ID:-1000}  
ENV GROUP_ID ${GROUP_ID:-1000}  
RUN groupadd -g ${GROUP_ID} monero  
RUN useradd -u ${USER_ID} -g monero -s /bin/bash -m -d /monero monero  
  
RUN chown monero:monero -R /monero  
  
RUN apt-get update && apt-get install -y curl bzip2 \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD https://dlsrc.getmonero.org/cli/monero-linux-x64-v0.12.0.0.tar.bz2 /tmp/  
RUN tar -xjvf /tmp/monero-linux-x64-v0.12.0.0.tar.bz2 -C /tmp/ \  
&& cp /tmp/monero-v0.12.0.0/* /usr/local/bin \  
&& rm -rf /tmp/monero-linux-x64-v0.12.0.0.tar.bz2  
  
ADD ./bin /usr/local/bin  
RUN chmod a+x /usr/local/bin/*  
  
# For some reason, docker.io (0.9.1~dfsg1-2) pkg in Ubuntu 14.04 has
permission  
# denied issues when executing /bin/bash from trusted builds. Building locally  
# works fine (strange). Using the upstream docker (0.11.1) pkg from  
# http://get.docker.io/ubuntu works fine also and seems simpler.  
USER monero  
  
VOLUME ["/monero"]  
  
EXPOSE 18080 18081 38080 38081  
WORKDIR /monero  
  
CMD ["xmr_oneshot"]  

