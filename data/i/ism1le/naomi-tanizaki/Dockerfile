FROM ubuntu:xenial  
  
RUN apt update  
RUN apt upgrade -y  
RUN apt install -y curl  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt update  
RUN apt install -y build-essential ffmpeg git python nodejs yarn  
RUN apt install -y libcairo2-dev libjpeg8-dev libpango1.0-dev libgif-dev g++
libtool autoconf automake  
RUN yarn global add node-gyp  
RUN apt autoremove -y  
  
RUN mkdir -p /usr/src/NT  
WORKDIR /usr/src/NT  
  
COPY . .  
  
RUN yarn install  
  
ENV TOKEN= \  
COMMAND_PREFIX= \  
COMMANDO_VERSION= \  
OAUTH_LINK= \  
OSU_API_KEY= \  
CLEVERBOT_API_USER= \  
CLEVERBOT_API_KEY= \  
ANILIST_ID= \  
ANILIST_SECRET= \  
SHIKIMORI_API_KEY= \  
PERMITTED_GROUP= \  
OWNERS= \  
DB= \  
REDIS= \  
EXAMPLE_CHANNEL= \  
ISSUE_CHANNEL= \  
REQUEST_CHANNEL= \  
WEATHER_API= \  
GOOGLE_API= \  
GOOGLE_CUSTOM_SEARCH= \  
GOOGLE_CUSTOM_SEARCH_CX= \  
SOUNDCLOUD_API= \  
SHERLOCK_API= \  
PAGINATED_ITEMS= \  
DEFAULT_VOLUME= \  
MAX_LENGTH= \  
MAX_SONGS= \  
PASSES=  
  
CMD node bot.js

