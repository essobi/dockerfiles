FROM node:0.10  
# Set up sharelatex user and home directory  
RUN adduser --system --group --home /var/lib/sharelatex \--no-create-home
sharelatex; \  
mkdir -p /var/lib/sharelatex; \  
chown sharelatex:sharelatex /var/lib/sharelatex; \  
mkdir -p /var/log/sharelatex; \  
chown sharelatex:sharelatex /var/log/sharelatex;  
  
WORKDIR /tmp  
  
RUN mkdir /tmp/install-tl-unx  
  
RUN wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz \  
&& tar -xf install-tl-unx.tar.gz -C ./install-tl-unx --strip-components=1  
  
COPY texlive.profile /tmp/install-tl-unx/  
RUN ./install-tl-unx/install-tl -profile ./install-tl-unx/texlive.profile \  
&& rm -r ./install-tl-unx \  
&& rm ./install-tl-unx.tar.gz  
  
RUN apt-get update \  
&& apt-get install -y \  
aspell aspell-en aspell-ru \  
build-essential \  
ghostscript \  
git \  
imagemagick \  
libkrb5-dev \  
optipng \  
python \  
qpdf \  
unzip \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
  
RUN git clone -b release https://github.com/sharelatex/sharelatex.git
/var/www/sharelatex  
  
WORKDIR /var/www/sharelatex  
RUN npm install -g grunt-cli \  
&& npm install \  
&& grunt install  
  
WORKDIR /var/www/sharelatex/web  
RUN grunt compile:minify  
  
ENV PATH $PATH:/usr/local/texlive/2017/bin/x86_64-linux/  
RUN tlmgr install \  
algorithm2e \  
algorithmicx \  
algorithms \  
bbm \  
bbm-macros \  
bbold \  
cancel \  
doublestroke \  
enumitem \  
ifplatform \  
mathabx \  
makecell \  
minted \  
mnsymbol \  
latexmk \  
relsize \  
shadethm \  
showlabels \  
srcltx \  
standalone \  
subfiles \  
titlesec \  
textpos \  
tocbibind \  
todonotes \  
yfonts \  
xstring  
  
VOLUME /var/lib/sharelatex  
  
COPY settings.coffee /etc/sharelatex/settings.coffee  
ENV SHARELATEX_CONFIG=/etc/sharelatex/settings.coffee  
  
WORKDIR /var/www/sharelatex  
ENTRYPOINT ["node"]  
USER sharelatex  
CMD []  

