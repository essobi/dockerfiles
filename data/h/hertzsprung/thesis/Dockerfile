FROM ubuntu:16.10  
MAINTAINER James Shaw <js102@zepler.net>  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
git \  
ca-certificates \  
make \  
rsync \  
texlive-latex-base \  
texlive-latex-recommended \  
texlive-latex-extra \  
texlive-fonts-recommended \  
texlive-fonts-extra \  
texlive-science \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN groupadd -r phd && \  
useradd -r -m -d /home/phd -s /sbin/nologin -g phd phd && \  
chown -R phd:phd /home/phd  
RUN mkdir -p /home/phd/build && chown phd:phd /home/phd/build  
USER phd  
  
ENV MAKE_COMMON=/home/phd/src/make-common  
  
RUN git clone --branch master https://github.com/hertzsprung/make-common.git
/home/phd/src/make-common \  
&& git clone --branch master https://github.com/hertzsprung/thesis.git
/home/phd/src/thesis  
  
WORKDIR /home/phd/src/thesis  
CMD ["make", "BUILD_DIR=/home/phd/build/thesis",
"/home/phd/build/thesis/thesis/thesis.pdf"]  

