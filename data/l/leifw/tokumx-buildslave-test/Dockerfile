FROM ubuntu:trusty  
RUN apt-get update  
RUN apt-get install -y build-essential ccache git cmake zlib1g-dev libboost-
dev libboost-filesystem-dev libboost-program-options-dev libboost-system-dev
libboost-thread-dev libpcap-dev libpcre3-dev libssl-dev libreadline-dev
debhelper devscripts buildbot-slave valgrind  
# hack to fake a real fuse installation because openjdk-7-jdk needs it  
# via https://gist.github.com/henrik-muehe/6155333  
RUN apt-get install libfuse2  
RUN cd /tmp ; apt-get download fuse  
RUN cd /tmp ; dpkg-deb -x fuse_* .  
RUN cd /tmp ; dpkg-deb -e fuse_*  
RUN cd /tmp ; rm fuse_*.deb  
RUN cd /tmp ; echo -en '#!/bin/bash\nexit 0\n' > DEBIAN/postinst  
RUN cd /tmp ; dpkg-deb -b . /fuse.deb  
RUN cd /tmp ; dpkg -i /fuse.deb  
RUN apt-get install -y python-dev python-nose ruby ruby-dev libsasl2-dev
openjdk-7-jdk maven cpanminus libdist-zilla-perl  
RUN REALLY_GEM_UPDATE_SYSTEM=1 gem update --system  
RUN gem install bundler  
RUN for lang in python ruby java perl; do git clone
https://github.com/Tokutek/mongo-$lang-driver; done  
RUN (cd mongo-python-driver; python2 setup.py install)  
RUN (cd mongo-ruby-driver; bundle install)  
RUN (cd mongo-java-driver; mvn test-compile)  
RUN (cd mongo-perl-driver; (dzil authordeps | cpanm -n) && (dzil listdeps |
cpanm -n))  
RUN cpanm --force Dist::Zilla::Plugin::SurgicalPodWeaver # tests fail, need
force  
RUN apt-get install -y scons  
RUN ln -s /lib/x86_64-linux-gnu/libcrypto.so.1.0.0 /lib/x86_64-linux-
gnu/libcrypto.so.6  
RUN ln -s /lib/x86_64-linux-gnu/libssl.so.1.0.0 /lib/x86_64-linux-
gnu/libssl.so.6  
WORKDIR /data  
CMD buildslave start && tail -f twistd.log  

