FROM ubuntu:14.04  
ENV SWIFT_BRANCH branch  
ENV SWIFT_VERSION 2.2  
ENV SWIFT_SNAPSHOT SNAPSHOT-2016-01-11-a  
ENV SWIFT_PLATFORM ubuntu14.04  
# Install related packages  
RUN apt-get update && \  
apt-get install -y build-essential wget libssl-dev clang libedit-dev python2.7
python2.7-dev libicu52 rsync git libpq-dev libxml2-dev postgresql postgresql-
contrib && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
USER postgres  
RUN /etc/init.d/postgresql start && \  
psql -d postgres -c "ALTER USER postgres WITH PASSWORD 'postgres';" && \  
createdb -O postgres todos  
  
USER root  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf  
  
EXPOSE 5432  
# Install Swift keys  
RUN wget -q -O - https://swift.org/keys/all-keys.asc | gpg --import - && \  
gpg --keyserver hkp://pool.sks-keyservers.net --refresh-keys Swift  
  
# Install Swift Ubuntu 14.04 Snapshot  
RUN SWIFT_ARCHIVE_NAME=swift-$SWIFT_VERSION-$SWIFT_SNAPSHOT-$SWIFT_PLATFORM &&
\  
SWIFT_URL=https://swift.org/builds/swift-$SWIFT_VERSION-$SWIFT_BRANCH/$(echo
"$SWIFT_PLATFORM" | tr -d
.)/swift-$SWIFT_VERSION-$SWIFT_SNAPSHOT/$SWIFT_ARCHIVE_NAME.tar.gz && \  
wget $SWIFT_URL && \  
wget $SWIFT_URL.sig && \  
gpg --verify $SWIFT_ARCHIVE_NAME.tar.gz.sig && \  
tar -xvzf $SWIFT_ARCHIVE_NAME.tar.gz --directory / --strip-components=1 && \  
rm -rf $SWIFT_ARCHIVE_NAME* /tmp/* /var/tmp/*  
  
# Set Swift Path  
ENV PATH /usr/bin:$PATH  
  
WORKDIR /tmp  
  
RUN git clone https://github.com/Zewo/libvenice.git && cd libvenice && \  
make && \  
make package && \  
dpkg -i libvenice.deb  
  
RUN git clone https://github.com/Zewo/http_parser.git && cd http_parser && \  
make && \  
make package && \  
dpkg -i http_parser.deb  
  
RUN git clone https://github.com/Zewo/uri_parser.git && cd uri_parser && \  
make && \  
make package && \  
dpkg -i uri_parser.deb  
  
RUN mkdir -p /var/app /workspace  
WORKDIR /var/app/  
  
RUN git clone https://github.com/Zewo/Examples.git  
  
WORKDIR /var/app/Examples  
  
RUN swift build  
  
EXPOSE 8080  
CMD /etc/init.d/postgresql start && .build/debug/Todo  

