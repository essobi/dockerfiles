FROM ubuntu:vivid  
MAINTAINER Hibou Corp. <hello@hibou.io>  
  
RUN set -x; \  
apt-get update \  
&& apt-get install -yq software-properties-common \  
&& apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0x5a16e7281be7a449  
  
## For modification to LTS release  
RUN add-apt-repository "deb http://dl.hhvm.com/ubuntu $(lsb_release
-sc)-lts-3.9 main"  
  
RUN apt-get update \  
&& apt-get install -yq --no-install-recommends \  
hhvm-dev \  
autoconf \  
automake \  
libtool \  
wget \  
unzip  
  
WORKDIR /var/lib/hhvm  
RUN mkdir extensions  
WORKDIR /var/lib/hhvm/extensions  
RUN mkdir mongodb && mkdir newrelic  
  
WORKDIR /var/lib/hhvm/extensions/mongodb  
RUN apt-get install -yq git \  
&& git clone \--branch r1.2 --depth 1 git://github.com/mongodb/libbson.git \  
&& cd libbson/ \  
&& ./autogen.sh \  
&& make \  
&& make install \  
&& cd .. \  
&& git clone https://github.com/mongofill/mongofill-hhvm \  
&& cd mongofill-hhvm \  
&& ./build.sh \  
&& ls -lah \  
&& cp ./mongo.so ../../ \  
&& cd ../../ \  
&& rm -rf ./mongodb  
  
WORKDIR /var/lib/hhvm/extensions/newrelic  
RUN wget
https://download.newrelic.com/agent_sdk/nr_agent_sdk-v0.16.1.0-beta.x86_64.tar.gz
\  
&& tar -xzf nr_agent_sdk-*.tar.gz \  
&& cp nr_agent_sdk-*/include/* /usr/local/include/ \  
&& cp nr_agent_sdk-*/lib/* /usr/local/lib/ \  
&& wget https://github.com/chregu/hhvm-newrelic-ext/archive/master.zip \  
&& unzip master.zip  
WORKDIR /var/lib/hhvm/extensions/newrelic/hhvm-newrelic-ext-master  
RUN hphpize \  
&& cmake . \  
&& make -j 2 \  
&& cp newrelic.so ../../  
WORKDIR /var/lib/hhvm/extensions  
RUN rm -rf ./newrelic  
  
RUN chown -R www-data:www-data /var/run/hhvm \  
&& chown -R www-data:www-data /var/log/hhvm  
  
WORKDIR /var/www  
  
USER www-data  
  
EXPOSE 9000  

