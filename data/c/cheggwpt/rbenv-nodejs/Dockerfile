FROM ubuntu:16.04  
LABEL maintainer="Joel Gilley jgilley@chegg.com"  
  
# use rbenv understandable version  
ARG RUBY_VERSION  
ENV RUBY_VERSION=${RUBY_VERSION:-2.5.0}  
  
ARG NODE_VERSION  
ENV NODE_VERSION=${NODE_VERSION:-8.6.0}  
  
ARG YARN_VERSION  
ENV YARN_VERSION=${YARN_VERSION:-latest}  
  
ARG DUMBINIT_VERSION  
ENV DUMBINIT_VERSION=${DUMBINIT_VERSION:-1.2.1}  
  
ARG TZ  
ENV TZ=${TZ:-Etc/UTC}  
  
# Set the timezone  
# Load ash profile on launch  
# Set rbenv in PATH for build  
# Set ruby ops for build  
ENV RBENV_ROOT=/usr/local/rbenv \  
NENV_ROOT=/usr/local/n \  
YARNENV_ROOT=/usr/local/yarn \  
RUBY_CONFIGURE_OPTS=--disable-install-doc \  
APP_ENV=development \  
RAILS_ENV=development  
  
# our custom path for the shims and various bin directories  
ENV
PATH=${RBENV_ROOT}/shims:${RBENV_ROOT}/bin:${YARNENV_ROOT}/bin:${NENV_ROOT}/bin:$PATH  
  
# Ruby's autoconf/configure doesn't detect macros properly so precaching these  
ENV ac_cv_func_isnan=yes \  
ac_cv_func_isinf=yes  
  
# Install needed libraries to build the things  
RUN apt-get update && \  
apt-get -y install tzdata build-essential git curl autoconf bison \  
libssl-dev libyaml-dev libreadline6-dev zlib1g-dev libncurses5-dev \  
libffi-dev libgdbm3 libgdbm-dev python nginx  
  
# set timezone to the time zone specified above  
RUN echo $TZ > /etc/timezone && \  
rm /etc/localtime && \  
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \  
dpkg-reconfigure -f noninteractive tzdata && \  
apt-get clean  
  
# setup nginx and puma directory  
RUN rm -rf /etc/nginx/nginx.conf /etc/nginx/sites-enabled/default && \  
mkdir -p /app /run/nginx /run/puma && \  
chown -R :www-data /run/nginx /run/puma /app && \  
chmod -R g+rw /run/nginx /run/puma /app  
  
# From now on we/re going to be working from /app  
WORKDIR /app  
  
# Install dumb-init for our pid 1 process reaping  
RUN cd /tmp && \  
curl -fsSL https://github.com/Yelp/dumb-
init/releases/download/v${DUMBINIT_VERSION}/dumb-
init_${DUMBINIT_VERSION}_amd64.deb -o dumb-init_${DUMBINIT_VERSION}_amd64.deb
&& \  
dpkg -i dumb-init_${DUMBINIT_VERSION}_amd64.deb && \  
rm -f dumb-init_${DUMBINIT_VERSION}_amd64.deb  
  
# Install N and Node  
RUN curl -fsSL https://git.io/n-install | N_PREFIX=${NENV_ROOT} bash -s -- -y
${NODE_VERSION}  
  
# install yarn  
RUN cd /tmp && \  
curl -fsSL https://yarnpkg.com/${YARN_VERSION}.tar.gz -o
yarn-${YARN_VERSION}.tgz && \  
mkdir ${YARNENV_ROOT} && \  
tar -xf yarn-${YARN_VERSION}.tgz -C ${YARNENV_ROOT} \--strip 1 && \  
rm yarn-${YARN_VERSION}.tgz;  
  
# install rbenv  
# setup the environment  
# check with the doctor  
# install ruby  
# install puma and bundler, and we run as root so silence that warning  
RUN git clone \--depth 1 https://github.com/rbenv/rbenv.git ${RBENV_ROOT} && \  
cd ${RBENV_ROOT} && \  
src/configure && \  
make -C src && \  
echo 'export RUBY_CONFIGURE_OPTS=--disable-install-doc' >> ~/.profile && \  
echo 'export PATH="${RBENV_ROOT}/bin:$PATH"' >> ~/.profile && \  
echo 'eval "$(rbenv init -)"' >> ~/.profile && \  
echo 'gem: --no-document' >> ~/.gemrc && \  
git clone \--depth 1 https://github.com/rbenv/ruby-build.git "$(rbenv
root)"/plugins/ruby-build && \  
curl -fsSL https://github.com/rbenv/rbenv-installer/raw/master/bin/rbenv-
doctor | bash && \  
rbenv install -v ${RUBY_VERSION} && \  
rbenv global ${RUBY_VERSION} && \  
gem install bundler puma && \  
bundle config git.allow_insecure true && \  
bundle config --global silence_root_warning 1  
  
# Add the container config files  
COPY ./container_configs /  
  
# Copy over the code Gemfile and run the install  
COPY ./code/Gemfile ./  
RUN chmod a+x /start-servers.sh && \  
bundle install  
  
# remove the build system  
# likely you're going to use your own Dockerfile inheriting this image  
# and repeat the above COPY and RUN to do your install  
# so this should probably be the last thing you run  
# RUN apk del build-deps  
# Finally copy over the app  
COPY ./code/ ./  
  
# expose our service port  
EXPOSE 80  
# start with our PID 1 controller  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
  
CMD ["/bin/sh", "-c", "/start-servers.sh"]  

