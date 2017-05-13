FROM kepler/kepler-base:latest

MAINTAINER Daniel Crawl <danielcrawl@gmail.com>

RUN echo 'xterm -e /kepler/biokepler-1.1/kepler.sh &' >> .vnc/xstartup

# get bioKepler
RUN curl http://www.biokepler.org/files/downloads/biokepler-1.1.tar.gz | tar xzf -
