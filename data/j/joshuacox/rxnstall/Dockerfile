FROM ubuntu:xenial  
  
ENV BUILD_PACKAGES='bash git wget curl locales tar nodejs npm ca-certificates'
\  
REACTION_ROOT='/home/reaction/reaction' \  
TOOL_NODE_FLAGS="--max-old-space-size=2048" \  
REACTIONSTALL_UPDATED=20171218  
RUN DEBIAN_FRONTEND=noninteractive \  
&& apt-get -qq update && apt-get -qqy dist-upgrade \  
&& apt-get -qqy --no-install-recommends install \  
$BUILD_PACKAGES \  
&& echo 'en_US.ISO-8859-15 ISO-8859-15'>>/etc/locale.gen \  
&& echo 'en_US ISO-8859-1'>>/etc/locale.gen \  
&& echo 'en_US.UTF-8 UTF-8'>>/etc/locale.gen \  
&& locale-gen \  
&& useradd -s /bin/sh -d /home/reaction reaction \  
&& mkdir -p /home/reaction \  
&& chown reaction. /home/reaction \  
&& apt-get remove -yqq nodejs npm \  
&& apt-get -y autoremove \  
&& apt-get clean \  
&& rm -Rf /var/lib/apt/lists/*  
  
COPY rxNstall /home/reaction/rxNstall  
RUN chown -R reaction:reaction /home/reaction  
  
USER reaction  
WORKDIR /home/reaction  
  
RUN /bin/bash -l ./rxNstall  
  
COPY test /test  
CMD [ "/test" ]  

