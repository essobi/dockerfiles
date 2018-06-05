FROM ubuntu:xenial  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
wget \  
curl \  
zip \  
git \  
openssh-client \  
unzip \  
vim \  
&& rm -rf /var/lib/apt/lists/*  
  
#Install Ruby and Cucumber  
ARG DEBIAN_FRONTEND=noninteractive  
  
ENV LANG_WHICH en  
ENV LANG_WHERE US  
ENV ENCODING UTF-8  
ENV LANGUAGE ${LANG_WHICH}_${LANG_WHERE}.${ENCODING}  
ENV LANG ${LANGUAGE}  
# Layer size: small: ~9 MB  
# Layer size: small: ~9 MB MB (with --no-install-recommends)  
RUN apt -qqy update \  
&& apt -qqy --no-install-recommends install \  
language-pack-en \  
tzdata \  
locales \  
&& locale-gen ${LANGUAGE} \  
&& dpkg-reconfigure --frontend noninteractive locales \  
&& apt -qyy autoremove \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt -qyy clean  
  
RUN apt-get update  
RUN apt-get install -y ruby2.3 ruby2.3-dev  
RUN apt-get install -y imagemagick libmagickwand-dev  
RUN apt-get install -y build-essential  
RUN apt -qyy clean  
  
RUN gem install bundler  
  
# avoid warning: Don't run Bundler as root  
RUN bundle config --global silence_root_warning 1  
  
# avoid warning: The gift source `git://github.com/dwbutler/logstash-
logger.git` uses the `git` protocol, which transmits data without encryption.
Disable this warning with `bundle config git.allow_insecure true`, or switch
to the `https` protocol to keep your data secure.  
RUN bundle config --global git.allow_insecure true  
  
ADD Gemfile* /  
RUN bundle install  
  
# set timezone  
ENV TZ=Europe/London  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ >
/etc/timezone=  
  
# install libs, xvfb and firefox  
RUN apt-get update && apt-get install -y zlib1g-dev xvfb libxcomposite1
libasound2 libdbus-glib-1-2 libgtk2.0-0  
  
ENV FF_LANG="en-US" \  
FF_BASE_URL="https://archive.mozilla.org/pub" \  
FF_PLATFORM="linux-x86_64" \  
FF_INNER_PATH="firefox/releases"  
#--- For Selenium 3  
# Layer size: big: 108.2 MB  
ARG FF_VER="49.0.1"  
ENV FF_COMP="firefox-${FF_VER}.tar.bz2"  
ENV
FF_URL="${FF_BASE_URL}/${FF_INNER_PATH}/${FF_VER}/${FF_PLATFORM}/${FF_LANG}/${FF_COMP}"  
RUN cd /opt \  
&& wget -nv "${FF_URL}" -O "firefox.tar.bz2" \  
&& bzip2 -d "firefox.tar.bz2" \  
&& tar xf "firefox.tar" \  
&& rm "firefox.tar" \  
&& ln -fs /opt/firefox/firefox /usr/bin/firefox \  
&& chmod -R 777 /opt/firefox  
  
LABEL selenium_firefox_version "${FF_VER}"  
  
#============  
# GeckoDriver  
#============  
# Layer size: tiny: ~4 MB  
ARG GECKOD_VER="0.14.0"  
ENV GECKOD_URL="https://github.com/mozilla/geckodriver/releases/download"  
RUN wget --no-verbose -O geckodriver.tar.gz \  
"${GECKOD_URL}/v${GECKOD_VER}/geckodriver-v${GECKOD_VER}-linux64.tar.gz" \  
&& rm -rf /opt/geckodriver* \  
&& tar -C /opt -xvzf geckodriver.tar.gz \  
&& cp /opt/geckodriver /usr/bin/geckodriver \  
&& rm geckodriver.tar.gz

