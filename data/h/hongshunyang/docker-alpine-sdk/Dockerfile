FROM hongshunyang/docker-alpine:3.6  
MAINTAINER Hongshun Yang<yanghongshun@outlook.com>  
  
## support edge main  
# update  
#RUN echo "@edge_main http://dl-4.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories  
#RUN echo "@edge_community http://dl-4.alpinelinux.org/alpine/edge/community"
>> /etc/apk/repositories  
ENV PACKAGER yanghongshun@outlook.com  
ENV PACKAGE_PRIVKEY_PUB ""  
ENV PACKAGE_PRIVKEY ""  
## dont chanage  
ENV REPODEST /home/builder/packages  
ENV APKBUILDS /home/builder/package  
  
RUN apk -U add alpine-sdk \  
&& adduser -G abuild -g "Alpine Package Builder" -s /bin/sh -D builder \  
&& echo "builder ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \  
&& rm -rf /var/cache/apk/*  
  
COPY entrypoint.sh /usr/local/bin/  
RUN chmod a+x /usr/local/bin/* \  
&& ln -s /usr/local/bin/entrypoint.sh /entrypoint.sh  
##  
COPY tmpl/_home_builder_.abuild_abuild.conf.tmpl
/home/builder/.abuild/abuild.conf.tmpl  
  
RUN chown -R builder /home/builder/ \  
&& touch /etc/apk/keys/alpine-abuild.rsa.pub \  
&& chown builder /etc/apk/keys/alpine-abuild.rsa.pub  
USER builder  
RUN mkdir -p $APKBUILDS \  
&& mkdir -p $REPODEST \  
&& dockerize -template
"/home/builder/.abuild/abuild.conf.tmpl:/home/builder/.abuild/abuild.conf"  
  
VOLUME ["$APKBUILDS","$REPODEST"]  
ENTRYPOINT ["/entrypoint.sh"]  
WORKDIR $APKBUILDS  
  

