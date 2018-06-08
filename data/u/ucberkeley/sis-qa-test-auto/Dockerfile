FROM ucberkeley/firefox-browser-gui  
  
MAINTAINER Dibyo Majumdar <dibyo.majumdar@gmail.com>  
  
USER root  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y curl \  
&& command curl -sSL https://rvm.io/mpapis.asc | gpg --import - \  
&& curl -sSL https://get.rvm.io | bash -s stable --ruby=jruby  
RUN usermod -a -G rvm developer  
  
RUN apt-get update && apt-get install -y python3-pip \  
&& pip3 install tornado  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y wget \  
&& wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.8-linux-x86_64.tar.bz2
\  
&& tar -xf phantomjs-1.9.8-linux-x86_64.tar.bz2 \  
&& cp phantomjs-1.9.8-linux-x86_64/bin/phantomjs /usr/bin \  
&& rm -r phantomjs-1.9.8-linux-x86_64*  
  
USER developer  
  
COPY Gemfile Gemfile.lock ${HOME}/  
RUN bash -c "\  
source /etc/profile.d/rvm.sh \  
&& cd ${HOME} \  
&& gem install bundle \  
&& bundle install --jobs 4 --retry 3"  
  
EXPOSE 8421  
COPY . /server/  
ENTRYPOINT ["/server/run_server.sh"]  

