#  
# ---- Base Node ----  
FROM jekyll/jekyll AS base  
WORKDIR /srv/jekyll  
  
#  
# ---- Build ----  
# run linters, setup, tests and build  
FROM base AS build  
COPY . .  
RUN mkdir -p /var/www && \  
chown -R jekyll:jekyll /var/www && \  
chown -R jekyll:jekyll /srv/jekyll && \  
/usr/local/bin/jekyll build --destination /var/www  
  
#  
# ---- Release ----  
FROM kyma/docker-nginx AS release  
COPY \--from=build /var/www /var/www  
CMD ["nginx"]

