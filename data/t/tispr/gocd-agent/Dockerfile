FROM openjdk:8  
ENV GOCD_VERSION 17.8.0-5277  
ENV GOCD_DISTR go-agent.deb  
  
# Install go.cd agent  
RUN curl -fSL https://download.gocd.io/binaries/${GOCD_VERSION}/deb/go-
agent_${GOCD_VERSION}_all.deb -o $GOCD_DISTR \  
&& dpkg -i $GOCD_DISTR \  
&& rm $GOCD_DISTR  
  
RUN mkdir /home/go \  
&& usermod -d /home/go go  
  
VOLUME /var/lib/go-agent  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["go-agent"]  

