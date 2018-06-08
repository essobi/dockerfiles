FROM ruby:2.3.1-slim  
  
MAINTAINER Thilo-Alexander Ginkel <tg@tgbyte.de>  
  
EXPOSE 10000 35729  
ENV RACK_ENV=production \  
RUN_AS=${UID:-www} \  
DUMBINIT_VERSION=1.1.3 \  
DUMBINIT_SHA256SUM=1af305fc011c72aa899c88fe6576e82f2c7657d8d5212a13583fd2de012e478f
\  
DEBIAN_FRONTEND=noninteractive \  
FOPUB_DIR=/opt/asciidoctor-fopub \  
PATH=/usr/local/bundle/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/asciidoctor-
fopub/bin \  
GRADLE_USER_HOME=/opt/gradle \  
BASENAME=slides  
  
ADD sources.list /etc/apt/  
RUN set -x \  
&& mkdir -p /home/slides/handouts \  
&& echo 'deb http://deb.debian.org/debian jessie-backports main' >
/etc/apt/sources.list.d/jessie-backports.list \  
&& apt-get update -qq \  
&& apt-get -t jessie-backports install -y --no-install-recommends \  
git \  
openjdk-8-jdk \  
ca-certificates-java \  
&& (echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula
select true | debconf-set-selections) \  
&& apt-get install -y -o Apt::Install-Recommends=0 \  
ca-certificates \  
fonts-liberation \  
ttf-mscorefonts-installer \  
inotify-tools \  
wget \  
xsltproc \  
&& wget -q -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v${DUMBINIT_VERSION}/dumb-
init_${DUMBINIT_VERSION}_amd64 \  
&& echo "${DUMBINIT_SHA256SUM} /usr/local/bin/dumb-init" > /tmp/SHA256SUM \  
&& sha256sum -c /tmp/SHA256SUM \  
&& rm /tmp/SHA256SUM \  
&& chmod +x /usr/local/bin/dumb-init \  
&& (cd /opt && git clone https://github.com/asciidoctor/asciidoctor-fopub &&
sed -i 's,dependencies {,dependencies {\nruntime
"org.apache.pdfbox:fontbox:1.8.13",' "${FOPUB_DIR}/build.gradle" &&
"${FOPUB_DIR}/gradlew" -p "$FOPUB_DIR" -q -u installApp) \  
&& apt-get remove -y --purge \  
wget \  
&& adduser --uid 500 --disabled-password --gecos "www" \--quiet www  
  
COPY Gemfile /home/slides/  
COPY Gemfile.lock /home/slides/  
WORKDIR /home/slides  
  
RUN set -x \  
&& apt-get install -y -o Apt::Install-Recommends=0 \  
build-essential \  
libssl-dev \  
python-pygments \  
&& bundle -j4 --without development test \  
&& apt-get remove -y --purge \  
build-essential \  
libssl-dev \  
&& apt-get autoremove -y --purge  
  
ADD . /home/slides  
RUN set -x \  
&& xsltproc --output /home/slides/docbook-xsl-custom/handout-titlepage.xsl
"${FOPUB_DIR}/build/fopub/docbook/template/titlepage.xsl"
/home/slides/docbook-xsl-custom/handout-titlepage.xml \  
&& mv /home/slides/generate /usr/local/bin \  
&& mv /home/slides/serve /usr/local/bin \  
&& mv /home/slides/handouts /usr/local/bin \  
&& mkdir -p /home/slides/slides \  
&& chown -R www.www /home/slides/slides  
  
USER www  
  
ENTRYPOINT ["/usr/local/bin/dumb-init"]  
CMD ["serve"]  
  
ONBUILD ARG UID  
ONBUILD ENV RUN_AS=${UID:-www}  
ONBUILD USER root  
ONBUILD ADD . /home/slides  
ONBUILD RUN generate && \  
chown -R $RUN_AS /home/slides  
ONBUILD USER $RUN_AS  

