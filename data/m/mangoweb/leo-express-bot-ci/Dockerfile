# available as https://hub.docker.com/r/mangoweb/leo-express-bot-ci/  
# to rebuild go to https://hub.docker.com/r/mangoweb/leo-express-bot-
ci/~/settings/automated-builds/  
  
FROM merorafael/php-cli:7.1  
  
# https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-
linux-distributions  
  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash \  
&& apt-get install -y \  
build-essential \  
nodejs \  
ssh \  
zip \  
&& env USER=root CFLAGS="-fPIC" CXXFLAGS="-fPIC" npm install -g mango-cli \  
&& nodejs --version && npm --version && mango --version  
  
RUN curl -o\- -L https://yarnpkg.com/install.sh | bash \  
&& ln -s "$HOME/.yarn/bin/yarn" /usr/bin/yarn \  
&& yarn --version  
  
# dependecy for npm flow  
RUN apt-get install -y \  
libelf-dev \  
ocaml  

