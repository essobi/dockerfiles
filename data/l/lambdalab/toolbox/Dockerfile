FROM debian:jessie  
RUN apt-get update  
  
RUN apt-get install -y curl redis-tools git python-pip  
  
ENV GPG_KEYS \  
# pub 4096R/A15703C6 2016-01-11 [expires: 2018-01-10]  
# Key fingerprint = 0C49 F373 0359 A145 1858 5931 BC71 1F9B A157 03C6  
# uid MongoDB 3.4 Release Signing Key <packaging@mongodb.com>  
0C49F3730359A14518585931BC711F9BA15703C6  
RUN set -ex; \  
export GNUPGHOME="$(mktemp -d)"; \  
for key in $GPG_KEYS; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done; \  
gpg --export $GPG_KEYS > /etc/apt/trusted.gpg.d/mongodb.gpg; \  
rm -r "$GNUPGHOME"; \  
apt-key list  
  
ENV MONGO_MAJOR 3.4  
ENV MONGO_VERSION 3.4.2  
RUN echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-
org/$MONGO_MAJOR main" > /etc/apt/sources.list.d/mongodb-org.list  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
mongodb-org-tools=$MONGO_VERSION mongodb-org-shell=$MONGO_VERSION \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/lib/mongodb  
  
RUN pip install --upgrade --user awscli  
RUN cp ~/.local/bin/aws /usr/bin  
  
RUN apt-get clean

