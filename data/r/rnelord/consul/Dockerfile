FROM buildpack-deps:trusty  
  
RUN apt-get update -qq && \  
apt-get install -y --no-install-recommends \  
netcat \  
unzip  
  
ENV CONSUL_VERSION 0.5.2  
ENV CONSUL_SHA256
171cf4074bfca3b1e46112105738985783f19c47f4408377241b868affa9d445  
  
EXPOSE 8300  
EXPOSE 8301 8301/udp  
EXPOSE 8302 8302/udp  
EXPOSE 8400  
EXPOSE 8500  
EXPOSE 8600  
EXPOSE 53/udp  
  
ADD https://dl.bintray.com/mitchellh/consul/${CONSUL_VERSION}_linux_amd64.zip
/tmp/consul.zip  
ADD https://dl.bintray.com/mitchellh/consul/${CONSUL_VERSION}_web_ui.zip
/tmp/consul-web_ui.zip  
  
RUN echo "${CONSUL_SHA256} /tmp/consul.zip" > /tmp/consul.sha256 \  
&& sha256sum -c /tmp/consul.sha256 \  
&& cd /usr/local/bin \  
&& unzip /tmp/consul.zip \  
&& chmod +x consul \  
&& rm /tmp/consul.zip  
  
RUN mkdir -p /usr/local/share/consul/ui \  
&& cd /usr/local/share/consul/ui \  
&& unzip /tmp/consul-web_ui.zip \  
&& mv dist/* . \  
&& rm -rf dist \  
&& rm /tmp/consul-web_ui.zip  
  
COPY config/ /etc/consul.d/  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
COPY scripts/ /usr/local/bin/  
  
# to allow people to bind mount custom scripts in to the container  
RUN mkdir -p /opt/local/bin /data  
VOLUME /opt/local/bin  
VOLUME /data  
  
RUN echo "PATH=\"/opt/local/bin:$PATH\"" >> /etc/profile  
ENV PATH
/opt/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["consul", "agent", "-config-dir=/etc/consul.d"]  

