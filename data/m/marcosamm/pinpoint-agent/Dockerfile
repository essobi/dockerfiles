# DESCRIPTION Pinpoint APM Agent Volume  
# TO_BUILD docker build -t pinpoint-agent .  
# TO_RUN docker run --name=pinpoint-agent pinpoint-agent  
FROM alpine:3.5  
ENV PINPOINT_VERSION=1.6.2  
ENV PINPOINT_AGENT_HOME /assets/pinpoint-agent  
  
ADD configure-agent.sh /usr/local/bin/  
  
RUN apk add --update curl bash \  
&& chmod a+x /usr/local/bin/configure-agent.sh \  
&& mkdir -p $PINPOINT_AGENT_HOME \  
&& curl -SL
https://github.com/naver/pinpoint/releases/download/$PINPOINT_VERSION/pinpoint-
agent-$PINPOINT_VERSION.tar.gz -o pinpoint-agent-$PINPOINT_VERSION.tar.gz \  
&& gunzip pinpoint-agent-$PINPOINT_VERSION.tar.gz \  
&& tar -xf pinpoint-agent-$PINPOINT_VERSION.tar -C $PINPOINT_AGENT_HOME \  
&& sed -i 's/DEBUG/INFO/' $PINPOINT_AGENT_HOME/lib/log4j.xml \  
&& rm pinpoint-agent-$PINPOINT_VERSION.tar \  
&& cd $PINPOINT_AGENT_HOME \  
&& mv pinpoint-bootstrap-$PINPOINT_VERSION.jar pinpoint-bootstrap.jar \  
&& apk del curl \  
&& rm /var/cache/apk/*  
  
VOLUME [$PINPOINT_AGENT_HOME]  
  
ENTRYPOINT ["/usr/local/bin/configure-agent.sh"]  
CMD ["tail -f /dev/null"]  

