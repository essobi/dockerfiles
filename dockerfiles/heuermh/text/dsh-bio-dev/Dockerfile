FROM sjackman/linuxbrew
MAINTAINER Michael Heuer <heuermh@acm.org>

USER root
RUN apt-get update && apt-get install -y \
  openjdk-7-jdk

USER linuxbrew
RUN brew install maven \
  && git clone https://github.com/heuermh/dishevelled-bio.git \
  && cd dishevelled-bio \
  && mvn package

ENV PATH /home/linuxbrew/dishevelled-bio/tools/target/appassembler/bin:$PATH

ENTRYPOINT ["dsh-bio"]
CMD ["--help"]
