FROM node:4.4-slim  
  
MAINTAINER Astorsoft <contactme@throughgithub.com>  
  
RUN apt-get update && apt-get install -y git  
RUN groupadd -r slides && useradd -r -g slides slides  
  
RUN git clone https://github.com/hakimel/reveal.js.git /revealjs  
RUN mkdir -p /revealjs/md  
  
WORKDIR /revealjs  
  
RUN npm install -g grunt-cli && npm install  
RUN sed -i Gruntfile.js -e "s/files: \\[ 'index\\.html'\\]/files: [ 'pres\/**'
]/"  
  
COPY index.html /revealjs/  
COPY content.md /revealjs/  
COPY dim.css /revealjs/css/  
COPY title.js /revealjs/plugin/  
COPY amtheme.css /revealjs/css/theme/  
COPY plugin/ /revealjs/plugin  
COPY audio/ reveal/audio  
  
RUN chown -R slides /revealjs  
USER slides  
  
EXPOSE 8000 35729  
CMD ["grunt", "serve"]  

