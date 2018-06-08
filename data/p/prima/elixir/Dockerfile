FROM msaraiva/erlang:18.3  
MAINTAINER Andrea Usuelli <andrea.usuelli@prima.it>  
  
ENV ELIXIR_VERSION 1.3.2  
  
RUN apk --update add unzip \  
ca-certificates \  
erlang-xmerl \  
erlang-crypto \  
erlang-ssl \  
erlang-public-key \  
erlang-asn1 \  
erlang-sasl \  
erlang-inets \  
erlang-erl-interface \  
erlang-runtime-tools \  
ncurses-libs \  
groff \  
less \  
python \  
py-pip \  
curl \  
tar \  
gzip \  
vim \  
tzdata && \  
  
cp /usr/share/zoneinfo/UTC /etc/localtime && \  
echo "Etc/UTC" > /etc/timezone && \  
  
update-ca-certificates && \  
curl -L -O https://github.com/elixir-
lang/elixir/releases/download/v${ELIXIR_VERSION}/Precompiled.zip && \  
mkdir -p /opt/elixir-${ELIXIR_VERSION}/ && \  
unzip Precompiled.zip -d /opt/elixir-${ELIXIR_VERSION}/ && \  
rm Precompiled.zip && \  
pip install awscli && \  
apk --purge del py-pip unzip wget tzdata && \  
rm -rf /var/cache/apk/*  
  
COPY files/setup_common.sh /setup_common.sh  
  
ENV PATH $PATH:/opt/elixir-${ELIXIR_VERSION}/bin  
  
ENTRYPOINT ["/bin/sh"]  

