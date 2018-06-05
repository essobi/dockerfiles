FROM debian:stretch-slim  
  
ARG agraph_version=6.4.1  
# This can be used to move all data files (e.g. to a volume)  
ENV AGRAPH_DATA_DIR=/data  
  
RUN apt-get update && apt-get install -y bzip2 libssl1.0-dev gettext-base
debianutils  
  
ADD
https://franz.com/ftp/pri/acl/ag/ag${agraph_version}/linuxamd64.64/agraph-${agraph_version}-linuxamd64.64.tar.gz
/tmp/agraph.tar.gz  
  
RUN tar zxf /tmp/agraph.tar.gz -C /tmp \  
&& /tmp/agraph-${agraph_version}/install-agraph --no-configure /app/agraph \  
&& rm -rf /tmp/agraph.tar.gz /tmp/agraph-${agraph_version}  
  
# Add mecab configuration (should not be needed with AG 6.4.2+)  
COPY mecabrc /etc/mecabrc  
  
# Copy config and entrypoint fragments.  
COPY docker.entrypoint.d /etc/docker.entrypoint.d  
COPY agraph.conf.d /etc/agraph.conf.d  
  
# Also do this when building a derived image  
ONBUILD COPY docker.entrypoint.d/* /etc/docker.entrypoint.d/  
ONBUILD COPY agraph.conf.d/* /etc/agraph.conf.d/  
  
COPY entrypoint.sh /  
CMD ["/entrypoint.sh"]  
  
EXPOSE 10000-10034 10035

