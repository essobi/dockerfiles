FROM ubuntu:xenial  
RUN apt-get update && apt-get upgrade && apt-get install -y ruby-dev build-
essential git  
RUN cd /usr/local/lib && git clone https://github.com/sass/sassc.git --depth 1
&& git clone https://github.com/sass/libsass.git --depth 1  
RUN cd /usr/local/lib && export SASS_LIBSASS_PATH="/usr/local/lib/libsass" &&
make -C libsass && make -C sassc && make -C sassc install  
RUN gem update --system  
RUN gem install listen  
RUN gem install sass --no-user-install  
RUN gem install bourbon neat bitters  
VOLUME /src  
WORKDIR /src  
ENTRYPOINT [ "sass" ]  

