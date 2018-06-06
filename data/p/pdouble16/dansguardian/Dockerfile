FROM blitznote/debootstrap-amd64:16.04  
MAINTAINER Patrick Double <pat@patdouble.com>  
  
ARG BUILD_DATE  
ARG SOURCE_COMMIT  
ARG DOCKERFILE_PATH  
ARG SOURCE_TYPE  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.dockerfile="$DOCKERFILE_PATH/Dockerfile" \  
org.label-schema.license="Apache-2.0" \  
org.label-schema.name="Container for DansGuardian, a web content filter" \  
org.label-schema.url="https://github.com/double16/dansguardian" \  
org.label-schema.vcs-ref=$SOURCE_COMMIT \  
org.label-schema.vcs-type="$SOURCE_TYPE" \  
org.label-schema.vcs-url="https://github.com/double16/dansguardian.git" \  
org.label-schema.vendor="https://github.com/double16"  
  
RUN rm -rf /var/lib/apt/lists/* && apt-get -q update &&\  
apt-get install -y --allow-downgrades --fix-broken --no-upgrade squid
dansguardian apache2 sarg wget cron psmisc netcat-openbsd &&\  
apt-get clean &&\  
usermod -aG users dansguardian &&\  
usermod -aG users proxy &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -rf /tmp/*  
  
# blacklist update  
COPY blacklist-update.sh /  
RUN chmod u+x /blacklist-update.sh && ln -s /blacklist-update.sh
/etc/cron.weekly/blacklist-update.sh && /bin/sh -x /blacklist-update.sh && cp
/blacklists/banned*list /etc/dansguardian/lists/  
  
# squid config  
COPY squid/* /etc/squid/  
# sarg (squid access reports) config  
RUN sed -i -e 's/output_dir .*/output_dir \/log\/sarg/' -e 's/access_log
.*/access_log \/log\/squid3\/access.log/' -e 's/^resolve_ip.*/resolve_ip yes/'
/etc/sarg/sarg.conf && sed -i -e 's/HTMLOUT=.*/HTMLOUT=\/log\/sarg/'
/etc/sarg/sarg-reports.conf && ln -sf /log/sarg /var/www/html/reports  
# dansguardian config  
RUN sed -i -e 's/filterport.*/filterport = 3128/' -e 's/proxyport.*/proxyport
= 8123/' -e 's/forwardedfor = .*/forwardedfor = on/' -e
's/#loglocation.*/loglocation = \/log\/dansguardian\/access.log/' -e
's/UNCONFIGURED/#UNCONFIGURED/' /etc/dansguardian/dansguardian.conf  
# logrotate  
COPY logrotate.d/* /etc/logrotate.d/  
COPY logrotate.conf /etc/logrotate.conf  
# apache conf  
RUN sed -i "s/Listen 80/Listen 8125/" /etc/apache2/ports.conf && sed -i
"s/:80>/:8125>/" /etc/apache2/sites-enabled/000-default.conf  
RUN ln -s /etc/apache2/mods-available/cgi.load /etc/apache2/mods-enabled/  
  
COPY ./start.sh ./healthcheck.sh /  
RUN chmod u+x /*.sh  
  
VOLUME [ "/blacklists", "/cache", "/log" ]  
  
# 3128 is the content filtered proxy port  
# 8123 is the caching only proxy port  
# 8124 is the transparent caching only proxy port  
# 8125 is the apache2 port serving the usage reports  
EXPOSE 3128 8123 8124 8125  
CMD ["/start.sh"]  
  
HEALTHCHECK \--interval=200s --timeout=100s CMD /healthcheck.sh || exit 1  
  

