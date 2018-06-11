FROM ruby:2.2  
MAINTAINER Andrei Gliga  
  
ENV MONGO_RELEASE_FINGERPRINT DFFA3DCF326E302C4787673A01C4E7FAAAB2461C  
RUN gpg --keyserver pgp.mit.edu --recv-keys $MONGO_RELEASE_FINGERPRINT  
  
ENV MONGO_VERSION 2.6.7  
VOLUME /data/db  
  
RUN apt-get update  
RUN apt-get install --yes nodejs locales  
  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen  
RUN locale-gen en_US.UTF-8  
ENV LANG "en_US.UTF-8"  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN curl -SL "https://fastdl.mongodb.org/linux/mongodb-
linux-x86_64-$MONGO_VERSION.tgz" -o mongo.tgz \  
&& curl -SL "https://fastdl.mongodb.org/linux/mongodb-
linux-x86_64-$MONGO_VERSION.tgz.sig" -o mongo.tgz.sig \  
&& gpg --verify mongo.tgz.sig \  
&& tar -xvf mongo.tgz -C /usr/local \--strip-components=1 \  
&& rm mongo.tgz*  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD RUN gem install thin  
ONBUILD COPY Gemfile /usr/src/app/  
ONBUILD COPY Gemfile.lock /usr/src/app/  
ONBUILD RUN bundle install  
  
ONBUILD COPY . /usr/src/app  
  
EXPOSE 3000  
CMD mongod & \  
bundle exec thin start -p 3000 -e production  

