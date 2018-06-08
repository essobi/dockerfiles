FROM debian:jessie  
  
ENV APP_DIR=/opt/ghf-markdown-preview  
  
COPY Gemfile \  
Gemfile.lock \  
${APP_DIR}/  
  
RUN apt-get update \  
&& RUNTIME_DEPS=' \  
pandoc \  
ruby2.1 \  
ruby2.1-dev \  
rubygems \  
' \  
GIT_DEPS=' \  
ca-certificates \  
git \  
' \  
OTHER_DEPS=' \  
build-essential \  
wget \  
' \  
BUILD_DEPS="${GIT_DEPS} ${OTHER_DEPS}" \  
GITHUB_MARKDOWN_CSS_BRANCH=v2.2.1 \  
&& apt-get install -y --no-install-recommends ${RUNTIME_DEPS} ${BUILD_DEPS} \  
&& cd ${APP_DIR} \  
&& gem install bundler --no-document \  
&& (echo 'install: --no-document'; echo 'update: --no-document') >
$HOME/.gemrc \  
&& bundle install \  
&& git clone -b ${GITHUB_MARKDOWN_CSS_BRANCH} \--depth 1
https://github.com/sindresorhus/github-markdown-css \  
&& ln -svf github-markdown-css/github-markdown.css . \  
&& apt-get purge -y ${BUILD_DEPS} \  
&& apt-get autoremove -y \  
&& apt-get install -y --no-install-recommends ${RUNTIME_DEPS} \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR ${APP_DIR}  
  
COPY preview.css \  
preview.js \  
template.sh \  
${APP_DIR}/  
RUN sh ./template.sh  
  
COPY Guardfile \  
Procfile \  
Rakefile \  
filter.sh \  
template.sh \  
${APP_DIR}/  
  
EXPOSE 35729 35730  
CMD ["foreman", "start"]  

