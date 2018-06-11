FROM ubuntu:xenial  
MAINTAINER Kyle Manna <kyle@kylemanna.com>  
  
ARG USER_ID  
ARG GROUP_ID  
  
ENV HOME /zcash  
  
# add user with specified (or default) user/group ids  
ENV USER_ID ${USER_ID:-1000}  
ENV GROUP_ID ${GROUP_ID:-1000}  
RUN groupadd -g ${GROUP_ID} zcash  
RUN useradd -u ${USER_ID} -g zcash -s /bin/bash -m -d /zcash zcash  
  
RUN chown zcash:zcash -R /zcash  
  
RUN apt-get update && apt-get install -y wget libdigest-sha-perl libgomp1 \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget -O zcash.tar.gz https://z.cash/downloads/zcash-1.1.0-linux64.tar.gz \  
&& tar -xzvf zcash.tar.gz -C /tmp/ && rm zcash.tar.gz \  
&& cp /tmp/zcash-*/bin/* /usr/local/bin \  
&& rm -rf /tmp/zcash-*  
  
ADD ./bin /usr/local/bin  
RUN chmod a+x /usr/local/bin/*  
  
# For some reason, docker.io (0.9.1~dfsg1-2) pkg in Ubuntu 14.04 has
permission  
# denied issues when executing /bin/bash from trusted builds. Building locally  
# works fine (strange). Using the upstream docker (0.11.1) pkg from  
# http://get.docker.io/ubuntu works fine also and seems simpler.  
USER zcash  
  
VOLUME ["/zcash"]  
  
EXPOSE 8232 8233 18232 18233  
WORKDIR /zcash  
  
CMD ["zec_oneshot"]  

