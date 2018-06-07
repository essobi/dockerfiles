FROM debian:stretch-slim  
  
ARG HORIZON_VERSION="0.12.3"  
# Install runtime dependencies and utils. Create man folders to workaround
this issue with debian stretch-slim
https://github.com/debuerreotype/debuerreotype/issues/10  
RUN apt-get update && mkdir -p /usr/share/man/man1 /usr/share/man/man7 \  
&& apt-get install -y --no-install-recommends curl ca-certificates postgresql-
client \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install horizon  
RUN curl -sL -o horizon.tar.gz
https://github.com/stellar/go/releases/download/horizon-v${HORIZON_VERSION}/horizon-v${HORIZON_VERSION}-linux-
amd64.tar.gz \  
&& tar -zxvf horizon.tar.gz \  
&& mv /horizon-v${HORIZON_VERSION}-linux-amd64/horizon /usr/local/bin \  
&& chmod +x /usr/local/bin/horizon \  
&& rm -rf horizon.tar.gz /horizon-v${HORIZON_VERSION}-linux-amd64  
  
# HTTP port  
EXPOSE 8000  
ADD entry.sh /  
  
ENTRYPOINT ["/entry.sh"]  
CMD ["horizon"]  

