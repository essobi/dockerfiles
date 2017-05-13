#
# 1Science container to build scala / sbt apps
#
FROM java:8
RUN apt-get update
RUN apt-get install -y wget vim

RUN cd /tmp

# install sbt
RUN apt-get update
RUN apt-get install -y --force-yes libpq-dev

ENV SBT_OPTS="-Xms512M -Xmx1536M -Xss1M -XX:+CMSClassUnloadingEnabled"
RUN echo "deb http://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823
RUN apt-get update
RUN apt-get install -y --force-yes sbt

RUN apt-get update
RUN apt-get install -y \
    python-dev \
    python-pip \
    libncurses5-dev

RUN apt-get install -y freetds-dev

ADD requirements.txt /dependencies/
RUN pip install -r /dependencies/requirements.txt

# requirement for codecov
RUN pip install codecov

WORKDIR /app

# Define default command.
CMD ["bash"]
