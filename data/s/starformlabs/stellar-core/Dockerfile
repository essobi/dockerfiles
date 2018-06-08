FROM debian:stretch-slim  
  
ARG STELLAR_CORE_VERSION="9.2.0-551-7561c1d5"  
ARG CONFD_VERSION="0.15.0"  
# Install runtime dependencies and utils. Create man folders to workaround
this issue with debian stretch-slim
https://github.com/debuerreotype/debuerreotype/issues/10  
RUN apt-get update && mkdir -p /usr/share/man/man1 /usr/share/man/man7 \  
&& apt-get install -y --no-install-recommends libpq5 libsqlite3-0 curl ca-
certificates postgresql-client \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install stellar-core  
RUN curl -sL -o stellar-core.deb
https://s3.amazonaws.com/stellar.org/releases/stellar-core/stellar-
core-${STELLAR_CORE_VERSION}_amd64.deb \  
&& dpkg -i stellar-core.deb \  
&& rm stellar-core.deb  
  
# Install confd for config file management  
RUN curl -sL -o /usr/local/bin/confd
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 \  
&& chmod +x /usr/local/bin/confd  
  
# Peer port (11625) and HTTP port (11626) (do NOT expose HTTP port publicly)  
EXPOSE 11625  
EXPOSE 11626  
COPY confd /etc/confd  
COPY entry.sh /  
  
ENTRYPOINT ["/entry.sh"]  
CMD ["/usr/local/bin/stellar-core", "--conf", "/stellar-core.cfg"]  

