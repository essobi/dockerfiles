FROM rails  
  
ENV DISCOURSE_VERSION 1.5.2  
ENV HOMEDIR /var/www/discourse  
  
RUN curl --silent --location https://deb.nodesource.com/setup_4.x | bash -  
  
# The above will do an apt-get update  
RUN apt-get install -yqq --no-install-recommends \  
libxml2 \  
nodejs \  
wget \  
runit \  
&& npm install uglify-js -g \  
&& npm install svgo -g \  
&& apt-get install -yqq --no-install-recommends \  
advancecomp jhead jpegoptim libjpeg-turbo-progs optipng  
  
RUN mkdir /jemalloc && cd /jemalloc \  
&& wget http://www.canonware.com/download/jemalloc/jemalloc-3.6.0.tar.bz2 \  
&& tar -xjf jemalloc-3.6.0.tar.bz2 && cd jemalloc-3.6.0 && ./configure && make
\  
&& mv lib/libjemalloc.so.1 /usr/lib && cd / && rm -rf /jemalloc  
  
COPY install-imagemagick /tmp/install-imagemagick  
RUN /tmp/install-imagemagick  
  
# Validate install  
RUN ruby -e "v='`convert -version`'; ['png','tiff','jpeg','freetype'].each{
|f| ((STDERR.puts('no ' + f + ' support in imagemagick')); exit(-1)) unless
v.include?(f)}"  
  
COPY install-pngcrush /tmp/install-pngcrush  
RUN /tmp/install-pngcrush  
  
COPY install-gifsicle /tmp/install-gifsicle  
RUN /tmp/install-gifsicle  
  
COPY install-pngquant /tmp/install-pngquant  
RUN /tmp/install-pngquant  
  
COPY install-nginx /tmp/install-nginx  
RUN /tmp/install-nginx  
  
# Discourse specific bits  
RUN useradd discourse -s /bin/bash -m -U &&\  
mkdir -p /var/www && cd /var/www &&\  
git clone https://github.com/discourse/discourse.git &&\  
cd discourse &&\  
git remote set-branches --add origin tests-passed &&\  
chown -R discourse:discourse $HOMEDIR &&\  
cd $HOMEDIR &&\  
bundle install --deployment \  
\--without test \--without development &&\  
find $HOMEDIR/vendor/bundle -name tmp -type d -exec rm -rf {} +  
  
RUN cd $HOMEDIR \  
&& mkdir -p tmp/pids \  
&& mkdir -p tmp/sockets \  
&& touch tmp/.gitkeep \  
&& mkdir -p /shared/log/rails \  
&& bash -c "touch -a
/shared/log/rails/{production,production_errors,unicorn.stdout,unicorn.stderr}.log"
\  
&& bash -c "ln -s
/shared/log/rails/{production,production_errors,unicorn.stdout,unicorn.stderr}.log
$HOMEDIR/log" \  
&& bash -c "mkdir -p /shared/{uploads,backups}" \  
&& bash -c "ln -s /shared/{uploads,backups} $HOMEDIR/public" \  
&& chown -R discourse .  
  
COPY nginx.conf /etc/nginx/conf.d/discourse.conf  
  
RUN sed -i "s/pid \/run\/nginx.pid\;/daemon off\;/" /etc/nginx/nginx.conf  
  
RUN rm /etc/nginx/sites-enabled/default \  
&& mkdir -p /var/nginx/cache  
  
COPY service /etc/service  
  
COPY policy.xml /usr/local/etc/ImageMagick-6/policy.xml  
  
COPY rake /usr/local/bin/rake  
  
RUN rm -rf /var/lib/apt/lists/*  
  
ENV RAILS_ENV production  
ENV RUBY_GC_MALLOC_LIMIT 90000000  
ENV DISCOURSE_DB_HOST postgres  
ENV DISCOURSE_REDIS_HOST redis  
ENV UNICORN_WORKERS 3  
ENV UNICORN_SIDEKIQS 1  
EXPOSE 80  
CMD ["/usr/bin/runsvdir", "-P", "/etc/service"]  

