FROM debian:wheezy  
  
ENV FONTFORGE_RELEASE 20141014  
ENV FONTFORGE_GIT_REPO https://github.com/fontforge/fontforge.git  
  
# install dependencies  
RUN apt-get update \  
&& apt-get install -y python-dev locales giflib-dbg libjpeg-dev \  
libtiff-dev libpango1.0-dev libspiro-dev libglib2.0-dev libxml2-dev \  
uthash-dev pkg-config \  
&& sed -e 's|^# en_US.UTF-8|en_US.UTF-8|g' -i /etc/locale.gen \  
&& sed -e 's|^# zh_TW.UTF-8|zh_TW.UTF-8|g' -i /etc/locale.gen \  
&& locale-gen  
  
# build fontforge from source  
RUN buildDeps="git packaging-dev"; \  
set -x \  
&& apt-get install -y $buildDeps \  
&& git clone "$FONTFORGE_GIT_REPO" \--branch "$FONTFORGE_RELEASE" \--single-
branch \  
&& cd fontforge \  
&& ./bootstrap \  
&& ./configure \  
&& make \  
&& make install \  
&& ldconfig \  
&& cd .. \  
&& rm -rf fontforge \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
  
# install and configure ipython  
RUN IPYTHON_CONFIG="c.InteractiveShellApp.exec_lines = ['import fontforge']";
\  
IPYTHON_CONFIG_FILE=/root/.ipython/profile_default/ipython_config.py; \  
wget https://bootstrap.pypa.io/get-pip.py \  
&& python get-pip.py \  
&& pip install ipython \  
&& ipython profile create \  
&& echo "$IPYTHON_CONFIG" >> "$IPYTHON_CONFIG_FILE"  
  
CMD [ "ipython" ]  

