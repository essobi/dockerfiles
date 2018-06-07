FROM node:6.11.5  
RUN echo "deb http://ftp.ru.debian.org/debian/ jessie-backports main contrib
non-free" > /etc/apt/sources.list.d/backports.list && \  
echo "deb http://ftp.ru.debian.org/debian/ jessie main contrib non-free" >
/etc/apt/sources.list && \  
echo "deb http://ftp.ru.debian.org/debian/ jessie-updates main contrib non-
free" >> /etc/apt/sources.list &&\  
echo "deb http://security.debian.org jessie/updates main contrib non-free" >>
/etc/apt/sources.list  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y -qq --no-install-recommends wget
unzip python php5-mysql php5-cli php5-cgi openssh-client python-openssl &&
apt-get clean  
  
RUN apt-get update && apt-get install locales-all -y \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update && apt-get install -t jessie-backports -y \  
openjdk-8-jdk \  
git \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV CLOUDSDK_PYTHON_SITEPACKAGES 1  
RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip
&& unzip google-cloud-sdk.zip && rm google-cloud-sdk.zip  
RUN google-cloud-sdk/install.sh --usage-reporting=false \--path-update=true
\--bash-completion=true \--rc-path=/.bashrc --additional-components app-
engine-java app-engine-python app kubectl alpha beta gcd-emulator pubsub-
emulator cloud-datastore-emulator app-engine-go bigtable  
  
# Disable updater check for the whole installation.  
# Users won't be bugged with notifications to update to the latest version of
gcloud.  
RUN google-cloud-sdk/bin/gcloud config set \--installation
component_manager/disable_update_check true  
  
# Disable updater completely.  
# Running `gcloud components update` doesn't really do anything in a union FS.  
# Changes are lost on a subsequent run.  
RUN sed -i -- 's/\"disable_updater\": false/\"disable_updater\": true/g'
/google-cloud-sdk/lib/googlecloudsdk/core/config.json  
  
ENV LEIN_VERSION=2.7.1  
ENV LEIN_INSTALL=/usr/local/bin/  
  
WORKDIR /tmp  
  
# Download the whole repo as an archive  
RUN mkdir -p $LEIN_INSTALL \  
&& wget -q
https://github.com/technomancy/leiningen/archive/$LEIN_VERSION.tar.gz \  
&& echo "Comparing archive checksum ..." \  
&& echo "876221e884780c865c2ce5c9aa5675a7cae9f215 *$LEIN_VERSION.tar.gz" |
sha1sum -c - \  
  
&& mkdir ./leiningen \  
&& tar -xzf $LEIN_VERSION.tar.gz -C ./leiningen/ --strip-components=1 \  
&& mv leiningen/bin/lein-pkg $LEIN_INSTALL/lein \  
&& rm -rf $LEIN_VERSION.tar.gz ./leiningen \  
  
&& chmod 0755 $LEIN_INSTALL/lein \  
  
# Download and verify Lein stand-alone jar  
&& wget -q
https://github.com/technomancy/leiningen/releases/download/$LEIN_VERSION/leiningen-$LEIN_VERSION-
standalone.zip \  
&& wget -q
https://github.com/technomancy/leiningen/releases/download/$LEIN_VERSION/leiningen-$LEIN_VERSION-
standalone.zip.asc \  
  
&& gpg --keyserver pool.sks-keyservers.net --recv-key
2E708FB2FCECA07FF8184E275A92E04305696D78 \  
&& echo "Verifying Jar file signature ..." \  
&& gpg --verify leiningen-$LEIN_VERSION-standalone.zip.asc \  
  
# Put the jar where lein script expects  
&& rm leiningen-$LEIN_VERSION-standalone.zip.asc \  
&& mkdir -p /usr/share/java \  
&& mv leiningen-$LEIN_VERSION-standalone.zip
/usr/share/java/leiningen-$LEIN_VERSION-standalone.jar  
  
ENV PATH=$PATH:$LEIN_INSTALL  
ENV LEIN_ROOT 1  
# Install clojure 1.8.0 so users don't have to download it every time  
RUN echo '(defproject dummy "" :dependencies [[org.clojure/clojure "1.8.0"]])'
> project.clj \  
&& lein deps && rm project.clj  
  
RUN ln -s /google-cloud-sdk/bin/gcloud /bin/gcloud  
RUN npm install -g firebase-tools phantomjs #trigger  

