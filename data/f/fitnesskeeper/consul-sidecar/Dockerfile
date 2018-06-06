FROM alpine:3.6  
# This is the release of Consul to pull in.  
ENV CONSUL_VERSION=1.0.6  
# This is the location of the releases.  
ENV HASHICORP_RELEASES=https://releases.hashicorp.com  
RUN apk -v --update add \  
bash \  
python \  
py-pip \  
groff \  
less \  
mailcap \  
jq \  
curl \  
ca-certificates \  
gnupg libcap \  
openssl \  
su-exec \  
dumb-init \  
&& \  
pip install --upgrade awscli==1.14.5 s3cmd==2.0.1 python-magic && \  
apk -v --purge del py-pip && \  
rm /var/cache/apk/*  
# Set up certificates, and Consul.  
RUN gpg --keyserver pgp.mit.edu --recv-keys
91A6E7F85D05C65630BEF18951852D87348FFC4C && \  
mkdir -p /tmp/build && \  
cd /tmp/build && \  
wget
${HASHICORP_RELEASES}/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip
&& \  
wget
${HASHICORP_RELEASES}/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_SHA256SUMS
&& \  
wget
${HASHICORP_RELEASES}/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_SHA256SUMS.sig
&& \  
gpg --batch --verify consul_${CONSUL_VERSION}_SHA256SUMS.sig
consul_${CONSUL_VERSION}_SHA256SUMS && \  
grep consul_${CONSUL_VERSION}_linux_amd64.zip
consul_${CONSUL_VERSION}_SHA256SUMS | sha256sum -c && \  
unzip -d /bin consul_${CONSUL_VERSION}_linux_amd64.zip && \  
cd /tmp && \  
rm -rf /tmp/build && \  
apk del gnupg openssl && \  
rm -rf /root/.gnupg  
  
COPY scripts/*.sh /usr/local/bin/  
COPY check_definitions/*.sh /usr/local/bin/check_definitions/  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
RUN mkdir /consul_check_definitions  
#RUN /usr/local/bin/create_check.sh > /consul_check_definitions/docker-
test.json  
VOLUME /root/.aws  
VOLUME /consul_check_definitions  
ENTRYPOINT ["docker-entrypoint.sh"]  

