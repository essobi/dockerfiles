FROM bvlc/caffe:cpu  
  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev curl
rsync postgresql vim git imagemagick locales gnupg2  
RUN curl --silent --location https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get update -qq && apt-get install -y nodejs  
  
# install debian packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qq \  
&& apt-get install --no-install-recommends -y \  
# install essentials  
build-essential \  
g++ \  
git \  
openssh-client \  
# install python 2  
python \  
python-dev \  
python-pip \  
python-setuptools \  
python-virtualenv \  
python-wheel \  
pkg-config \  
# requirements for numpy  
libopenblas-base \  
python-numpy \  
python-scipy \  
# requirements for keras  
python-h5py \  
python-yaml \  
python-pydot \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ARG TENSORFLOW_VERSION=1.3.0  
ARG TENSORFLOW_DEVICE=cpu  
ARG TENSORFLOW_APPEND=  
RUN pip --no-cache-dir install
https://storage.googleapis.com/tensorflow/linux/${TENSORFLOW_DEVICE}/tensorflow${TENSORFLOW_APPEND}-${TENSORFLOW_VERSION}-cp27-none-
linux_x86_64.whl  
  
ARG KERAS_VERSION=2.0.8  
ENV KERAS_BACKEND=tensorflow  
RUN pip --no-cache-dir install --no-dependencies
git+https://github.com/fchollet/keras.git@${KERAS_VERSION}  
  
# quick test and dump package lists  
RUN python -c "import tensorflow; print(tensorflow.__version__)" \  
&& dpkg-query -l > /dpkg-query-l.txt \  
&& pip2 freeze > /pip2-freeze.txt  
  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3
7D2BAF1CF37B13E2069D6956105BD0E739499BDB  
RUN \curl -L https://get.rvm.io | bash -s stable  
RUN /bin/bash -l -c "rvm requirements"  
RUN /bin/bash -l -c "rvm install 2.4.1"  
  
RUN echo 'ru_RU.UTF-8 UTF-8' >> /etc/locale.gen  
RUN locale-gen ru_RU.UTF-8  
RUN dpkg-reconfigure -fnoninteractive locales  
ENV LC_ALL=ru_RU.utf8  
ENV LANGUAGE=ru_RU.utf8  
RUN update-locale LC_ALL="ru_RU.utf8" LANG="ru_RU.utf8" LANGUAGE="ru_RU"  
  
RUN /bin/bash -l -c "gem install bundler"  
  
RUN npm install -g yarn webpack  
RUN mkdir -p /apps/gusar  
RUN curl -L 'https://www.dropbox.com/s/54qsc9q5g4vuczo/model.h5?dl=1' >
/apps/model.h5  
  
WORKDIR /apps/gusar  
COPY package.json package.json  
COPY yarn.lock yarn.lock  
RUN yarn install  
  
COPY Gemfile Gemfile  
COPY Gemfile.lock Gemfile.lock  
RUN /bin/bash -l -c "bundle install --jobs 4"  
  
ADD . /apps/gusar  
ADD config/database.example.yml config/database.yml  
  
EXPOSE 80  
ENV RAILS_SERVE_STATIC_FILES true  
ENV RAILS_ENV production  
ENV NODE_ENV production  
ENV HOSTNAME http://rails.gusar.1cb9d70e.svc.dockerapp.io/  
  
RUN mkdir /apps/gusar/public/uploads  
VOLUME /apps/gusar/public/uploads  
  
RUN /bin/bash -l -c "bundle exec rails webpacker:compile"  
RUN /bin/bash -l -c "rake assets:precompile"  
  
EXPOSE 80  
CMD /bin/bash -l -c "bundle exec rails s -p 80 -b '0.0.0.0'"  

