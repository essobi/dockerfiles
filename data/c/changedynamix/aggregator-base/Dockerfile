FROM openjdk:8-jre  
  
ADD native_libs/stripped_libhadoop.tgz /  
  
RUN echo /usr/local/lib >> /etc/ld.so.conf  
  
RUN apt-get update; apt-get install libsodium18 libunwind8; cd
/etc/apt/sources.list.d; wget http://build.sageaxcess.com/apt/sageaxcess-
repo.list; echo "Package: fgetty\nPin: release *\nPin-Priority: -1" >
/etc/apt/preferences; apt-get update; apt-get install -y --force-yes -t
sageaxcess libsodium libzmq jzmq; DEBIAN_FRONTEND=noninteractive apt-get
install -y runit inotify-tools; apt-get clean; rm -R /var/lib/apt/lists
/etc/apt/preferences /var/log/* /var/lib/dpkg/* /var/lib/apt/extended_states
/var/cache/ldconfig/aux-cache /usr/share/man/man8/run* /usr/share/man/man8/sv*
/usr/share/man/man8/update-service.8.gz /usr/share/man/man8/utmpset.8.gz
/usr/share/doc/libzmq /usr/share/doc/libsodiu* /usr/share/doc/libinotifytools0
/usr/share/doc/inotify-tools /usr/local/lib/*.a /usr/local/lib/*.la
/usr/local/lib/pkgconfig/* /usr/local/include/zmq* /usr/local/include/sodiu*;  
  
ENTRYPOINT ["/sbin/runsvdir -P /etc/sv"]  

