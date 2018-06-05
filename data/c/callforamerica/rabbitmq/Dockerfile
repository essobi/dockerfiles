FROM callforamerica/debian  
  
MAINTAINER Joe Black <joeblack949@gmail.com>  
  
ARG ERLANG_VERSION  
ARG RABBITMQ_VERSION  
  
ENV ERLANG_VERSION=${ERLANG_VERSION:-19.2}  
ENV RABBITMQ_VERSION=${RABBITMQ_VERSION:-3.6.6}  
  
LABEL lang.erlang.version=$ERLANG_VERSION  
LABEL app.rabbitmq.version=$RABBITMQ_VERSION  
  
ENV APP rabbitmq  
ENV USER $APP  
ENV HOME /var/lib/$APP  
  
COPY build.sh /tmp/  
RUN /tmp/build.sh  
  
COPY entrypoint /  
  
ENV ERL_MAX_PORTS 65536  
ENV RABBITMQ_LOG_LEVEL info  
  
EXPOSE 5672 15672  
VOLUME ["/var/lib/rabbitmq/mnesia"]  
  
WORKDIR $HOME  
  
SHELL ["/bin/bash"]  
HEALTHCHECK \--interval=15s --timeout=5s \  
CMD bash -lc "rabbitmqctl node_health_check | grep -q '^Health check passed'
|| exit 1"  
  
ENTRYPOINT ["/dumb-init", "--"]  
CMD ["/entrypoint"]  

