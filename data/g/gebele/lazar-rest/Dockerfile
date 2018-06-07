FROM base/archlinux  
MAINTAINER Denis Gebele <gebele@in-silico.ch>  
  
RUN pacman-db-upgrade && pacman -Syyu --noconfirm && pacman -S --noconfirm \  
base-devel \  
boost-libs \  
cmake \  
eigen3 \  
fontconfig \  
gcc-fortran \  
git \  
gsl \  
jre7-openjdk-headless \  
mongodb \  
mongodb-tools \  
r \  
ruby \  
swig \  
vim \  
wget && pacman -Scc --noconfirm  
  
RUN useradd -ms /bin/bash ist  
RUN echo "ist ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
RUN mkdir -p /data/db  
USER ist  
WORKDIR /home/ist  
  
RUN wget https://cran.r-project.org/src/contrib/Rserve_1.7-3.tar.gz -O Rserve  
RUN sudo R CMD INSTALL Rserve  
  
RUN echo 'gem: --user-install --no-document' > ~/.gemrc  
ENV PATH $PATH:/home/ist/.gem/ruby/2.5.0/bin  
RUN export GEM_HOME=$(ruby -e 'print Gem.user_dir')  
RUN gem install bundler  
RUN bundle config --global silence_root_warning 1  
  
RUN git clone https://github.com/opentox/lazar.git && \  
cd lazar && \  
git checkout "ORN" && \  
ruby ext/lazar/extconf.rb && \  
bundle install --path ~/.gem  
  
RUN git clone https://github.com/opentox/qsar-report.git && \  
cd qsar-report && \  
git checkout "development" && \  
bundle install --path ~/.gem  
  
RUN git clone https://github.com/opentox/lazar-public-data.git  
  
RUN git clone https://github.com/opentox/lazar-rest.git && \  
cd lazar-rest && \  
git checkout "ORN" && \  
bundle install --path ~/.gem  
  
RUN git clone https://github.com/opentox/lazar-gui.git && \  
cd lazar-gui && \  
git checkout "development" && \  
bundle install --path ~/.gem  
  
RUN git clone https://github.com/swagger-api/swagger-ui.git  
COPY index.html /home/ist/swagger-ui/dist/index.html  
  
COPY start.sh /home/ist/start.sh  
WORKDIR /home/ist  
RUN sudo chmod +x /home/ist/start.sh  
ENTRYPOINT ["/home/ist/start.sh"]  
  

