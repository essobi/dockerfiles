FROM swipl as base  
  
RUN apt-get update && apt-get install -y \  
git build-essential autoconf curl unzip \  
node-requirejs  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
RUN npm install -g bower clean-css clean-css-cli  
  
ENV SWISH_HOME /swish  
WORKDIR ${SWISH_HOME}  
  
ENV SWISH_SHA1 8f82e1fccf11f17fdc8821ad8d6066b5973000cc  
RUN echo "At version ${SWISH_SHA1}"  
RUN git clone https://github.com/vre4eic/swish.git ${SWISH_HOME} && \  
git checkout -q ${SWISH_SHA1}  
  
RUN bower install --allow-root  
RUN make -C /swish RJS="nodejs /usr/lib/nodejs/requirejs/r.js" \  
src packs min  
  
FROM base  
LABEL maintainer "Jan Wielemaker <jan@swi-prolog.org>", "Jacco van
Ossenbruggen <Jacco.van.Ossenbruggen@cwi.nl>"  
  
RUN apt-get update && apt-get install -y \  
graphviz imagemagick \  
wamerican && \  
rm -rf /var/lib/apt/lists/*  
  
COPY \--from=base /swish /swish  
COPY entry.sh /entry.sh  
  
ENV SWISH_DATA /data  
VOLUME ${SWISH_DATA}  
WORKDIR ${SWISH_DATA}  
  
ENTRYPOINT ["/entry.sh"]  

