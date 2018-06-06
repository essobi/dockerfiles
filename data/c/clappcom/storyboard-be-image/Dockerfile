FROM clappcom/nginx-php-jesse:latest  
  
MAINTAINER PENCEO hi@penceo.com  
  
RUN apt-get update && apt-get install -y curl gnupg git  
  
COPY scripts/install_ffmpeg_with_aac.sh /  
RUN chmod +x install_ffmpeg_with_aac.sh && sleep 1 &&
./install_ffmpeg_with_aac.sh  
  
# build audiowaveform  
RUN apt-get install -y make cmake gcc g++ libmad0-dev libid3tag0-dev
libsndfile1-dev libgd2-xpm-dev libboost-filesystem-dev libboost-program-
options-dev libboost-regex-dev  
RUN git clone https://github.com/bbc/audiowaveform.git /audiowaveform  
RUN cd /audiowaveform && mkdir build && cd build && cmake -D ENABLE_TESTS=0 ..
&& make \  
&& cp audiowaveform /usr/share/nginx/html  
  
RUN cd ~ && curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs build-essential python2.7 supervisor  
RUN apt-get install -y libcairo2-dev libjpeg62-turbo-dev libpango1.0-dev
libgif-dev build-essential g++  
RUN rm -f /usr/bin/python && ln -s /usr/bin/python2.7 /usr/bin/python  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
RUN apt-get update && apt-get install yarn  
  
# Install ts-node to run typescript files  
RUN yarn global add ts-node  
# Install a TypeScript compiler (requires `typescript` by default).  
RUN yarn global add typescript  
RUN yarn global add @angular/cli  
  
COPY vhosts /vhosts  

