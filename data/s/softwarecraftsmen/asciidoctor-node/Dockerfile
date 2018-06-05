FROM alpine  
  
LABEL maintainer "david.loidolt@software-craftsmen.at"  
LABEL maintainer "martin.ahrer@software-craftsmen.at"  
LABEL org.label-schema.vendor="Software Craftsmen Gmbh & Co KG" \  
org.label-schema.name="jenkins-master" \  
org.label-schema.description="Jenkins Master" \  
org.label-schema.usage="${vcs_url}" \  
org.label-schema.url="${vcs_url}" \  
org.label-schema.vcs-url=$vcs_url \  
org.label-schema.vcs-branch=$vcs_branch \  
org.label-schema.vcs-ref=$vcs_ref \  
org.label-schema.version=$version \  
org.label-schema.schema-version="1.0" \  
org.label-schema.build-date=$build_date  
  
ENV LIBRARY_PATH=/lib:/usr/lib  
ENV ASCIIDOCTOR_VERSION "1.5.5"  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
  
RUN apk add --update --no-cache \  
gcc \  
g++ \  
make \  
bash \  
curl \  
unzip \  
tar \  
openjdk8-jre \  
ruby-dev \  
ruby \  
ruby-nokogiri \  
ruby-json \  
python \  
python-dev \  
py-setuptools \  
py-pip \  
ttf-dejavu \  
libjpeg-turbo \  
libjpeg-turbo-dev \  
zlib \  
zlib-dev \  
nodejs \  
nodejs-npm \  
git \  
graphviz \  
&& gem install --no-ri --no-rdoc rake slim \  
&& gem install --no-ri --no-rdoc asciidoctor --version $ASCIIDOCTOR_VERSION \  
&& gem install --no-ri --no-rdoc asciidoctor-diagram \  
&& gem install --no-ri --no-rdoc asciidoctor-revealjs \  
&& gem cleanup \  
&& pip install "blockdiag[pdf]" \  
&& pip install seqdiag \  
&& pip install actdiag \  
&& pip install nwdiag \  
&& apk del bash curl unzip tar gcc g++ make ruby-dev python-dev py-pip
libjpeg-turbo-dev zlib-dev \  
&& rm -rf /tmp/* /var/cache/apk/* ~/.cache/pip  
  
WORKDIR /documents  
VOLUME /documents  
  
CMD ["/bin/sh"]  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT /docker-entrypoint.sh  

