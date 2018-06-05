FROM node:latest  
  
ARG MONGO_PACKAGE=mongodb-org  
ARG MONGO_REPO=repo.mongodb.org  
ENV MONGO_PACKAGE=${MONGO_PACKAGE} MONGO_REPO=${MONGO_REPO}  
  
ENV MONGO_MAJOR 3.6  
ENV MONGO_VERSION 3.6.5  
ENV GPG_KEYS \  
# pub 4096R/91FA4AD5 2016-12-14 [expires: 2018-12-14]  
# Key fingerprint = 2930 ADAE 8CAF 5059 EE73 BB4B 5871 2A22 91FA 4AD5  
# uid MongoDB 3.6 Release Signing Key <packaging@mongodb.com>  
2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5  
# https://docs.mongodb.com/manual/tutorial/verify-mongodb-packages/#download-
then-import-the-key-file  
RUN set -ex; \  
export GNUPGHOME="$(mktemp -d)"; \  
for key in $GPG_KEYS; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done; \  
gpg --export $GPG_KEYS > /etc/apt/trusted.gpg.d/mongodb.gpg; \  
rm -r "$GNUPGHOME"; \  
apt-key list  
  
RUN echo "deb http://$MONGO_REPO/apt/debian
jessie/${MONGO_PACKAGE%-unstable}/$MONGO_MAJOR main" | tee
"/etc/apt/sources.list.d/${MONGO_PACKAGE%-unstable}.list"  
  
RUN apt-get update  
RUN apt-get install -y \  
${MONGO_PACKAGE}=$MONGO_VERSION \  
${MONGO_PACKAGE}-server=$MONGO_VERSION \  
${MONGO_PACKAGE}-shell=$MONGO_VERSION \  
${MONGO_PACKAGE}-mongos=$MONGO_VERSION \  
${MONGO_PACKAGE}-tools=$MONGO_VERSION  
  
RUN apt-get install -y python3-pip  
RUN pip3 install awscli  
  
ADD packages/migration/package.json /foodblogs-migration/  
ADD packages/migration/package-lock.json /foodblogs-migration/  
ADD packages/migration/dist /foodblogs-migration/  
ADD bin /usr/bin  
  
RUN cd /foodblogs-migration && npm i  

