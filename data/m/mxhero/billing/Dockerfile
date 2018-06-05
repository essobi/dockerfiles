FROM pierrevincent/gradle-java8  
MAINTAINER Juan Pablo Royo <juanpablo.royo@gmail.com>  
  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install wget  
RUN wget -O/etc/apt/sources.list.d/couchbase.list
http://packages.couchbase.com/ubuntu/couchbase-ubuntu1204.list  
RUN apt-get update  
RUN /bin/bash -l -c "wget -O-
http://packages.couchbase.com/ubuntu/couchbase.key | sudo apt-key add -"  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y --force-yes install g++ gcc make
python-software-properties wget openssl libreadline6 libreadline6-dev curl git
zlib1g zlib1g-dev libssl-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev
libxslt-dev autoconf libc6-dev ncurses-dev automake libtool bison subversion
zlib1g-dev build-essential libreadline-dev libsqlite3-dev libxml2-dev
libxslt1-dev git libcouchbase2-libevent libcouchbase-dev vim  
  
WORKDIR /opt/mxhero/billing  
  
RUN /bin/bash -l -c "git clone
https://mxheroinc:mx+hero@bitbucket.org/mxhero/billing.git
/opt/mxhero/billing"  
RUN /bin/bash -l -c "gradle build"  
  
RUN mkdir -p /override_lib && cp /etc/hosts /var/ && cp /lib/x86_64-linux-
gnu/libnss_files.so.2 /override_lib  
RUN sed -ie 's:/etc/hosts:/var/hosts:g' /override_lib/libnss_files.so.2  
ENV LD_LIBRARY_PATH /override_lib  
  
RUN /bin/bash -l -c "echo '10.50.1.177 couchbase-node-stage-2.mxhero.net
couchbase-stage.mxhero.net' >> /var/hosts"  
RUN /bin/bash -l -c "echo '10.50.1.178 couchbase-node-stage-3.mxhero.net
couchbase-stage.mxhero.net' >> /var/hosts"  
  
EXPOSE 8080  
ENTRYPOINT ["gradle"]  
CMD ["bootRun"]

