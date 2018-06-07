FROM ubuntu:14.04  
EXPOSE 8000  
RUN apt-get update && apt-get -y install git nodejs npm  
RUN apt-get update && apt-get -y install curl  
RUN apt-get update && apt-get -y install unionfs-fuse  
RUN apt-get update && apt-get -y install wget  
RUN apt-get update && apt-get -y install zip  
RUN apt-get update && apt-get -y install python-bs4  
  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN git clone https://github.com/hakimel/reveal.js.git  
WORKDIR reveal.js  
RUN git checkout 713702a0ab81d1756a30e6c14ae49afd42135541  
RUN npm install  
  
WORKDIR /  
RUN git clone https://github.com/astefanutti/decktape.git  
WORKDIR decktape  
RUN git checkout 42310835e3523093b80ced40914e992d55b692a4  
RUN mkdir -p bin  
RUN wget -O bin/phantomjs
http://astefanutti.github.io/decktape/downloads/phantomjs-linux-
ubuntu16-x86-64  
RUN chmod +x bin/phantomjs  
RUN apt-get update && apt-get -y install fontconfig libicu52  
  
WORKDIR /  
RUN git clone https://github.com/isagalaev/highlight.js.git  
WORKDIR /highlight.js  
RUN git checkout bb1cdfe052cd6c98e0d1d61f16dff9f1d2d57ffc  
WORKDIR /  
RUN cp /highlight.js/src/styles/* /reveal.js/lib/css/  
  
WORKDIR /reveal.js/plugin  
RUN mkdir anything  
WORKDIR anything  
RUN wget -O anything.js https://github.com/rajgoel/reveal.js-
plugins/blob/545336f66d6f94214d92209721a7bd7547120b10/anything/anything.js  
  
WORKDIR /reveal.js/plugin  
RUN mkdir asciinema  
WORKDIR asciinema  
RUN wget -O asciinema-player.css https://github.com/asciinema/asciinema-
player/releases/download/v2.3.1/asciinema-player.css  
RUN wget -O asciinema-player.js https://github.com/asciinema/asciinema-
player/releases/download/v2.3.1/asciinema-player.js  
  
WORKDIR /reveal.js/plugin  
RUN mkdir viz  
RUN wget -O viz/viz.js
https://github.com/mdaines/viz.js/releases/download/v1.4.1/viz.js  
  
WORKDIR /reveal.js/plugin  
RUN wget https://github.com/mathjax/MathJax/archive/2.7.0.zip  
RUN unzip *.zip  
RUN rm *.zip  
RUN mv MathJax* MathJax  
  
WORKDIR /  
RUN git clone https://github.com/chjj/marked  
WORKDIR /marked  
RUN git checkout 38f1727ffee0820975677027b8968bc1954e6637  
RUN npm install  
COPY marked.columns.patch .  
RUN ls lib  
RUN patch -p1 < marked.columns.patch  
RUN ./node_modules/gulp/bin/gulp.js  
RUN mv ./marked.min.js /reveal.js/plugin/markdown/marked.js  
  
WORKDIR /reveal.js  
RUN npm install grunt-exec --save-dev  
COPY Gruntfile.patch .  
RUN patch < Gruntfile.patch  
  
WORKDIR /reveal.js/plugin/markdown  
COPY markdown.patch .  
RUN patch < markdown.patch  
  
WORKDIR /reveal.js/plugin/math  
COPY math.patch .  
RUN patch < math.patch  
  
WORKDIR /  
RUN mkdir slides  
RUN mkdir pres  
  
WORKDIR /  
COPY generate-index.py .  
RUN chmod +x generate-index.py  
COPY index.template /reveal.js  
COPY fuse .  
RUN chmod +x fuse  
COPY enter .  
RUN chmod +x enter  
COPY run .  
RUN chmod +x run  
COPY pdf .  
RUN chmod +x pdf  
COPY generate-index.py .  
RUN chmod +x generate-index.py .  

