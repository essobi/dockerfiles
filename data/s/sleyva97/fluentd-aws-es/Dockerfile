FROM gcr.io/google_containers/ubuntu-slim:0.6  
LABEL maintainer="sleyva1297@gmail.com"  
  
RUN ulimit -n 65536  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y -q --no-install-recommends curl ca-
certificates make g++ sudo bash  
  
RUN /usr/bin/curl -sSL https://toolbelt.treasuredata.com/sh/install-ubuntu-
xenial-td-agent2.sh | sh  
  
RUN sed -i -e "s/USER=td-agent/USER=root/" -e "s/GROUP=td-agent/GROUP=root/"
/etc/init.d/td-agent  
  
RUN td-agent-gem install --no-document fluent-plugin-
kubernetes_metadata_filter -v 0.32.0  
  
RUN td-agent-gem install --no-document fluent-plugin-kinesis -v 2.1.0  
  
RUN td-agent-gem install --no-document fluent-plugin-prometheus -v 1.0.1  
  
COPY td-agent.conf /etc/td-agent/td-agent.conf  
  
ENV LD_PRELOAD /opt/td-agent/embedded/lib/libjemalloc.so  
  
RUN apt-get remove -y make g++ && apt-get autoremove -y && apt-get clean -y &&
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["td-agent"]  

