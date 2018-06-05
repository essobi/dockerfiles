FROM nodebb/docker:v1.9.3  
WORKDIR /usr/src/app  
  
COPY watchdog.bash /usr/src/app/  
  
ENV NODE_ENV=production \  
daemon=false \  
silent=false  
  
RUN apt-get update \  
&& apt-get install -y webp \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN sed -e "s/var mediumMin = \\\\([0-9]\\\\+\\\\);/var mediumMin =
!window.localStorage['unresponsive-settings'] ||
JSON.parse(window.localStorage['unresponsive-settings']).responsive ? \\\1 :
0;/" -i /usr/src/app/node_modules/nodebb-plugin-composer-
default/static/lib/composer/resize.js  
  
COPY plugins /usr/src/app/plugins  
RUN npm install --save ./plugins/*/ nodebb-plugin-shortcuts@1.1.2 nodebb-
plugin-emoji@2.2.3  
  
RUN node -e 'require("nodebb-plugin-emoji-
one/emoji").defineEmoji({packs:[]},function(err){if(err){console.error(err);process.exit(1)}})'  
  
COPY emoji/tdwtf /usr/src/app/tdwtf-emoji  
RUN cd /usr/src/app/tdwtf-emoji && node -p 'var
dict={};fs.readdirSync(__dirname).filter(function(e){return
e!=="dictionary.json"}).forEach(function(e){dict[e.replace(/\\.[^.]+$/,"")]={aliases:[e],image:e}});JSON.stringify(dict)'
> /usr/src/app/tdwtf-emoji/dictionary.json  
COPY emoji/fontawesome.json /usr/src/app/tdwtf-emoji/  
  
RUN echo public/uploads/*/ > .make-uploads-folders  
  
# PULL REQUESTS  
# delete these steps as the pull requests get merged into the upstream repo  
RUN curl -sSL
https://github.com/BenLubar/NodeBB/commit/195a1c503a25b967be67d91297d234fb0170501b.diff
| patch -p1  
RUN cd node_modules/nodebb-plugin-tdwtf-buttons && curl -sSL https://patch-
diff.githubusercontent.com/raw/NedFodder/nodebb-plugin-tdwtf-
buttons/pull/2.diff | patch -p1  
RUN rm -rf node_modules/mubsub && cp -R node_modules/mubsub-nbb
node_modules/mubsub  
  
ADD iframely-date.diff /usr/src/app/node_modules/nodebb-plugin-iframely/  
RUN cd node_modules/nodebb-plugin-iframely && patch -p1 < iframely-date.diff  
  
VOLUME /usr/src/app/docker  
VOLUME /usr/src/app/public/uploads  
  
# save the config in a volume so the container can be discarded  
RUN ln -s /usr/src/app/docker/config.json /usr/src/app/config.json  
  
# make sure the uploads subdirectories exist, run any database migrations,  
# and set the container's process as the NodeBB daemon so ./nodebb works  
CMD cat .make-uploads-folders | xargs mkdir -p \  
&& ./nodebb upgrade --schema --build \  
&& echo 1 > pidfile \  
&& bash -c './watchdog.bash &' \  
&& exec node loader.js  

