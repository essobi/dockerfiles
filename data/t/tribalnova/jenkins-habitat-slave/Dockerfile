FROM jenkinsci/jnlp-slave  
MAINTAINER Dominique Rochefort <dominique.rochefort@hmhco.com>  
  
USER root  
  
# Silence some warnings while building the docker image  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb http://deb.debian.org/debian jessie non-free" >>
/etc/apt/sources.list && \  
echo "deb http://ftp.uk.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y \  
apt-utils jq ffmpeg zip dnsutils \  
python-setuptools \  
python-dev build-essential \  
software-properties-common  
  
# install sox with mp3 support  
RUN apt-get install libsox-fmt-mp3 sox -y  
  
# Install text-to-speech software  
RUN apt-get install libttspico0 libttspico-utils libttspico-data -y  
  
# Install Ruby and Sass  
RUN apt-get install -y ruby ruby-dev && \  
gem install sass  
  
# Install AWS CLI  
RUN easy_install pip && pip install awscli  
  
# Install Node 8  
ENV NPM_CONFIG_PREFIX="/home/jenkins/.npm"  
RUN mkdir -p /home/jenkins/.npm && \  
curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get install -y nodejs && \  
chown jenkins -R /home/jenkins  
  
# Install yarn: https://yarnpkg.com/lang/en/docs/install/#linux-tab  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && \  
apt-get install -y yarn  
  
ADD init-credentials.sh /usr/bin/init-credentials.sh  
RUN chmod a+x /usr/bin/init-credentials.sh  
  
# Install Chromium latest stable version  
RUN wget -q https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb && \  
apt-get install fonts-liberation libatk-bridge2.0-0 libgtk-3-0 xdg-utils -y &&
\  
apt-get install -f -y && \  
apt-get install libappindicator3-1 -y && \  
dpkg -i google-chrome-stable_current_amd64.deb  
  
USER jenkins  
  
# Install Node packages  
RUN npm i -g npm@latest  
RUN npm i bower grunt-cli gulp-cli -g  
  
# EXPLIB-1268 - bower-artifactory integration  
RUN npm i -g bower-art-resolver  
  
ENV PATH="/home/jenkins/.npm/bin:$PATH"  
# Add bitbucket and Github to the known hosts  
RUN mkdir -p /home/jenkins/.ssh && \  
ssh-keyscan -H bitbucket.org >> /home/jenkins/.ssh/known_hosts && \  
ssh-keyscan -H github.com >> /home/jenkins/.ssh/known_hosts  
  
# Add access to @hmh private npm registry  
RUN npm config set @hmh:registry http://npm.tribalnova.com  
  
# Create the SVN directory to hold SVN credentials  
RUN mkdir -p /home/jenkins/.subversion/auth/svn.simple  
  
# Install chrome-driver  
RUN npm install -g chromedriver  
  
# Launch as Jenkins slave with proper arguments  
ENTRYPOINT ["jenkins-slave"]  

