FROM vcatechnology/arch-ci:latest  
MAINTAINER VCA Technology <developers@vcatechnology.com>  
  
# Build-time metadata as defined at http://label-schema.org  
ARG PROJECT_NAME  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="$PROJECT_NAME" \  
org.label-schema.description="An up-to-date Arch Linux image with packages for
documentation building" \  
org.label-schema.url="https://www.archlinux.org/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/vcatechnology/docker-arch-
documentation" \  
org.label-schema.vendor="VCA Technology" \  
org.label-schema.version=$VERSION \  
org.label-schema.license=MIT \  
org.label-schema.schema-version="1.0"  
# Install packages  
RUN sudo vca-install-package \  
git \  
openssh \  
make \  
rsync \  
tar \  
bzip2 \  
gzip \  
xz \  
pandoc \  
python-blessings \  
python-pandocfilters \  
python-pypandoc \  
python-pip \  
optipng \  
python-pylint \  
yapf \  
jpegoptim \  
jq \  
texlive-most \  
npm  
# zopfli isn't in the main repositories anymore  
RUN sudo pacman --noprogressbar --noconfirm -U
https://archive.archlinux.org/packages/z/zopfli/zopfli-1.0.1-1-x86_64.pkg.tar.xz
\  
&& sudo sh -c 'yes | pacman --noprogressbar -Scc' \  
&& sudo pacman-optimize --nocolor  
  
# Install NPM packages  
RUN sudo npm install -g markdownlint-cli  
  
# Install Python packages  
RUN pip install --user inquirer  

