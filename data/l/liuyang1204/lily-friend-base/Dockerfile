FROM ruby:2.1.5  
# install Lilypond  
RUN curl -O
http://download.linuxaudio.org/lilypond/binaries/linux-64/lilypond-2.18.2-1.linux-64.sh
\  
&& sh lilypond-2.18.2-1.linux-64.sh \  
&& rm lilypond-2.18.2-1.linux-64.sh  
  
# install fluidsynth & lame  
RUN apt-get update \  
&& apt-get install -y fluidsynth lame fluid-soundfont-gm  
  
# throw errors if Gemfile has been modified since Gemfile.lock  
RUN bundle config --global frozen 1  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY Gemfile /usr/src/app/  
ONBUILD COPY Gemfile.lock /usr/src/app/  
ONBUILD RUN bundle install  
  
ONBUILD COPY . /usr/src/app  

