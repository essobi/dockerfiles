FROM alpine:3.2  
MAINTAINER Albert Dixon <albert@dixon.rocks>  
  
VOLUME ["/data"]  
RUN apk update \  
&& apk add --update --repository
http://dl-1.alpinelinux.org/alpine/edge/testing/ tini \  
&& apk add \  
ca-certificates \  
git \  
nodejs \  
openssl \  
sqlite  
  
ADD https://ghost.org/zip/ghost-latest.zip /ghost.zip  
RUN mkdir -v /ghost /themes \  
&& unzip -o /ghost.zip -d /ghost \  
&& rm -vf /ghost.zip /ghost/config.example.js \  
&& cd /ghost \  
&& npm install --production \  
&& npm install --global gulp \  
&& cp -r /ghost/content/* /data/  
  
# add tmplnator for template processing  
ADD
https://github.com/albertrdixon/tmplnator/releases/download/v2.2.1/t2-linux.tgz
/t2.tgz  
RUN tar xvzf /t2.tgz -C /usr/local/bin && rm -vf /t2.tgz  
  
# add gosu for setuid exec'ing  
ADD https://github.com/tianon/gosu/releases/download/1.7/gosu-amd64
/usr/local/bin/gosu  
  
# themes!  
# minto (please go sign up at http://alen-vuletic.from.hr/minto-theme/ for
full documentation)  
ADD http://alen-vuletic.from.hr/download/minto-ghost-v1.zip /minto.zip  
RUN unzip /minto.zip && mv -v /minto-theme/minto /themes/ \  
&& rm -rf /minto.zip /minto-theme  
# decode  
RUN git clone \--depth=1 https://github.com/ScottSmith95/Decode-for-Ghost.git
/themes/decode \  
&& cd /themes/decode \  
&& npm install \  
&& gulp build  
# readium  
RUN git clone \--depth=1 https://github.com/starburst1977/readium.git
/themes/readium  
# saga  
RUN git clone \--depth=1 https://github.com/Reedyn/Saga.git /themes/saga  
# ghostium  
RUN git clone \--depth=1 https://github.com/oswaldoacauan/ghostium.git
/themes/ghostium  
# ghostwriter  
RUN git clone \--depth=1 https://github.com/roryg/ghostwriter.git
/themes/ghostwriter  
# atilla  
RUN git clone \--depth=1 https://github.com/zutrinken/attila.git
/themes/atilla  
# phantom  
RUN git clone \--depth=1 https://github.com/haydenbleasel/ghost-themes.git
/themes/phantom \  
&& cd /themes/phantom && git checkout phantom  
# # cactus  
# RUN git clone --depth=1 https://github.com/haydenbleasel/ghost-themes.git
/themes/cactus \  
# && cd /themes/cactus && git checkout cactus  
# 8days  
RUN git clone \--depth=1 https://github.com/zohf/8-days-theme.git
/themes/8days  
# glimpse  
RUN git clone \--depth=1 https://github.com/bensventures/Glimpse.git
/themes/glimpse  
# placidity  
RUN git clone \--depth=1 https://github.com/DanielTamkin/placidity.git
/themes/placidity  
# mnml  
RUN git clone \--depth=1 https://github.com/curiositry/mnml-ghost-theme.git
/themes/mnml  
# hoist  
RUN git clone \--depth=1 https://github.com/EliotSlevin/hoist-ghost.git
/themes/hoist  
# pixeltraveller  
RUN git clone \--depth=1 https://github.com/Skepton/Pixeltraveller.git
/themes/pixeltraveller  
# portfolio  
RUN git clone \--depth=1 https://github.com/GavickPro/Portfolio-Free-Ghost-
Theme.git /themes/portfolio  
  
ADD *.tmpl /templates/  
ADD docker-* /usr/local/bin/  
RUN chmod +x /usr/local/bin/* \  
&& chown -R nobody /ghost  
  
ENTRYPOINT ["tini", "-g", "--", "docker-entry"]  
CMD ["docker-start"]  
  
ENV EXTERNAL_URL www.example.com  
ENV FORCE_ADMIN_SSL false  
ENV GHOST_PORT 8080  
ENV NODE_ENV production  

