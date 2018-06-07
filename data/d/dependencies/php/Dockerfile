FROM composer:1.6.5  
RUN apk --no-cache add git wget patch  
  
# add a non-root user and give them ownership  
RUN adduser -D -u 9000 app && \  
# repo  
mkdir /repo && \  
chown -R app:app /repo && \  
# app code  
mkdir /usr/src/app && \  
chown -R app:app /usr/src/app  
  
# add the deps utility to easily create pull requests on different git hosts  
WORKDIR /usr/src/app  
ENV DEPS_VERSION=2.3.0  
RUN wget https://github.com/dependencies-
io/deps/releases/download/${DEPS_VERSION}/deps_${DEPS_VERSION}_linux_amd64.tar.gz
&& \  
mkdir deps && \  
tar -zxvf deps_${DEPS_VERSION}_linux_amd64.tar.gz -C deps && \  
ln -s /usr/src/app/deps/deps /usr/local/bin/deps  
  
# run everything from here on as non-root  
USER app  
  
RUN git config --global user.email "bot@dependencies.io"  
RUN git config --global user.name "Dependencies.io Bot"  
  
# install requirements first, so we can cache this step  
RUN mkdir /usr/src/app/src  
ADD src/composer.json /usr/src/app/src  
ADD src/composer.lock /usr/src/app/src  
RUN cd /usr/src/app/src && composer install  
  
ADD src /usr/src/app/src  
  
WORKDIR /repo  
  
ENTRYPOINT ["php", "/usr/src/app/src/entrypoint.php"]  

