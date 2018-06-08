FROM node:4-slim  
MAINTAINER fschl <fschl.code@gmail.com>  
  
ENV REVEAL_VERSION 3.2.0  
RUN curl -SLO
"https://github.com/hakimel/reveal.js/archive/${REVEAL_VERSION}.tar.gz" \  
&& tar xzf ${REVEAL_VERSION}.tar.gz \  
&& mv /reveal.js-${REVEAL_VERSION} /revealjs \  
&& rm *.tar.gz  
  
RUN mkdir -p /revealjs/md  
  
RUN npm install grunt-cli -g  
  
WORKDIR /revealjs  
  
RUN npm install --only=prod  
  
RUN sed -i Gruntfile.js -e 's/port: port,/port: port, hostname: "",/' \  
&& grunt --force  
  
ADD title.js /revealjs/plugin/  
  
EXPOSE 8000  
VOLUME ["/revealjs/md/"]  
CMD ["grunt", "serve"]  
  
ONBUILD ADD index.html /revealjs/  
ONBUILD ADD slides.md /revealjs/md/  
ONBUILD ADD images/ /revealjs/images/  
ONBUILD ADD custom.css /revealjs/css/  

