FROM node:10-alpine  
  
#ENV CLJ_TOOLS_VERSION=1.9.0.381  
ENV LEIN_VERSION=2.8.1  
ENV MAVEN_VERSION=3.5.2  
ENV MAVEN_HOME=/usr/lib/mvn  
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true  
ENV LEIN_ROOT=1  
WORKDIR /tmp  
  
RUN apk update --verbose && apk upgrade --verbose && apk add --verbose
--upgrade \  
bash \  
build-base \  
ca-certificates \  
chromium \  
curl \  
docker \  
file \  
fontconfig \  
git \  
gnupg \  
jq \  
maven \  
ncurses \  
openjdk8 \  
openssh \  
openssl \  
postgresql \  
py3-pip \  
python3 \  
rsync \  
ruby \  
ruby-bundler \  
ruby-dev \  
ruby-irb \  
ruby-rdoc \  
tar \  
the_silver_searcher \  
util-linux \  
wget \  
zip \  
&& rm -rf /var/cache/apk  
  
#--- Leiningen (from https://github.com/sgerrand/alpine-pkg-leiningen)  
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
leiningen/master/sgerrand.rsa.pub \  
&& wget https://github.com/sgerrand/alpine-pkg-
leiningen/releases/download/${LEIN_VERSION}-r0/leiningen-${LEIN_VERSION}-r0.apk
\  
&& apk add --verbose leiningen-${LEIN_VERSION}-r0.apk  
  
#TODO: Uncomment when clj tools required (will need to install rlwrap)  
#--- Clojure-Tools  
#RUN curl -O https://download.clojure.org/install/linux-
install-${CLJ_TOOLS_VERSION}.sh \  
# && chmod +x linux-install-${CLJ_TOOLS_VERSION}.sh \  
# && ./linux-install-${CLJ_TOOLS_VERSION}.sh  
#--- Typical Node Tools  
RUN npm install --global --unsafe-perm \  
lumo-cljs \  
progress \  
cljs \  
gulp-cli \  
http-server \  
wait-on  
  
#--- Typical Ruby Tools  
RUN gem install \  
bundler  
  
#-- Typical Python Tools  
RUN ln -s /usr/bin/python3 /usr/bin/python \  
&& ln -s /usr/bin/pip3 /usr/bin/pip  
RUN pip3 install --upgrade pip && pip3 install --upgrade \  
colorama==0.3.7 \  
awscli \  
awsebcli \  
&& rm -rf ~/.cache/pip  
  
#-- Install CircleCI Tools  
RUN git clone -b master https://github.com/jesims/circleci-tools.git \  
&& cd circleci-tools \  
&& git pull \  
&& chmod +x ./cancel-redundant-builds.sh  
ENV PATH=$PATH:/tmp/circleci-tools/  
RUN node -v > .node_version  
  
CMD ["bash"]  
  
#TODO don't run as root  

