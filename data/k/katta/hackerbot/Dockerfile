FROM python:2-onbuild  
# docker build . --build-arg APT_PROXY="http://apt-proxy.local:3142" -t
katta/vacanze  
ARG APT_PROXY  
RUN [ -z "$APT_PROXY" ] || /bin/echo -e "Acquire::HTTP::Proxy
\"$APT_PROXY\";\nAcquire::HTTPS::Proxy
\"$APT_PROXY\";\nAcquire::http::Pipeline-Depth \"23\";" >
/etc/apt/apt.conf.d/01proxy  
  
# prepare  
ENV PYTHONUNBUFFERED 1  
RUN mkdir -p /app  
WORKDIR /app  
  
RUN set -x && \  
apt-get -qq update && \  
apt-get -y install curl && \  
curl -sL https://github.com/omergunal/hackerbot/archive/master.tar.gz | \  
tar xz -C /app --strip-components=1 && \  
sh install.sh && \  
apt-get clean all && \  
rm -rf /var/lib/apt/lists/*  
  
# entrypoint  
ADD entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT [ "/entrypoint.sh" ]

