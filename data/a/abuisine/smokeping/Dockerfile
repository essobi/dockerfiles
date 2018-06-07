FROM debian:stretch  
  
LABEL maintainer="Alexandre Buisine <alexandrejabuisine@gmail.com>"  
LABEL version="2.0.0"  
  
# Install lighttpd and smokeping  
RUN export DEBIAN_FRONTEND='noninteractive' \  
&& apt-get update -qq \  
&& apt-get install -qqy --no-install-recommends ca-certificates curl dnsutils
\  
echoping fonts-dejavu-core lighttpd procps smokeping ssmtp libnet-dns-perl \  
&& apt-get clean \  
&& sed -i '/^syslogfacility/s/^/#/' /etc/smokeping/config.d/General \  
&& conf=/etc/lighttpd/lighttpd.conf dir=/etc/lighttpd/conf-available \  
header=setenv.add-response-header \  
&& sed -i '/server.errorlog/s|^|#|' $conf \  
&& sed -i '/server.document-root/s|/html||' $conf \  
&& sed -i '/mod_rewrite/a\ \t"mod_setenv",' $conf \  
&& echo "\\\n$header"' += ( "X-XSS-Protection" => "1; mode=block" )' >>$conf \  
&& echo "$header"' += ( "X-Content-Type-Options" => "nosniff" )' >>$conf \  
&& echo "$header"' += ( "X-Robots-Tag" => "none" )' >>$conf \  
&& echo "$header"' += ( "X-Frame-Options" => "SAMEORIGIN" )' >>$conf \  
&& echo '\n$HTTP["url"] =~ "^/smokeping($|/)" {' >>$conf \  
&& echo '\tdir-listing.activate = "disable"\n}' >>$conf \  
&& echo '\n# redirect to the right Smokeping URI' >>$conf \  
&& echo 'url.redirect = ("^/$" => "/smokeping/smokeping.cgi",' >>$conf \  
&& echo '\t\t\t"^/smokeping/?$" => "/smokeping/smokeping.cgi")' >>$conf \  
&& sed -i 's|var/log/lighttpd/access.log|tmp/log|' $dir/10-accesslog.conf \  
&& sed -i '/^#cgi\\.assign/,$s/^#//; /"\\.pl"/i\ \t".cgi" => "/usr/bin/perl",'
\  
$dir/10-cgi.conf \  
&& echo '\nfastcgi.server += ( ".cgi" =>\n\t((' >>$dir/10-fastcgi.conf \  
&& sed -i -e '/CHILDREN/s/[0-9][0-9]*/16/' \  
-e '/max-procs/a\ \t\t"idle-timeout" => 20,' \  
$dir/15-fastcgi-php.conf \  
&& grep -q 'allow-x-send-file' $dir/15-fastcgi-php.conf || { \  
sed -i '/idle-timeout/a\ \t\t"allow-x-send-file" => "enable",' \  
$dir/15-fastcgi-php.conf \  
&& sed -i '/"bin-environment"/a\ \t\t\t"MOD_X_SENDFILE2_ENABLED" => "1",' \  
$dir/15-fastcgi-php.conf; } \  
&& echo '\t\t"socket" => "/tmp/perl.socket" + var.PID,' \  
>>$dir/10-fastcgi.conf \  
&& echo '\t\t"bin-path" => "/usr/lib/cgi-bin/smokeping.cgi",'\  
>>$dir/10-fastcgi.conf \  
&& echo '\t\t"docroot" => "/var/www",' >>$dir/10-fastcgi.conf \  
&& echo '\t\t"check-local" => "disable",\n\t))\n)' \  
>>$dir/10-fastcgi.conf \  
&& unset conf dir header \  
&& lighttpd-enable-mod cgi \  
&& lighttpd-enable-mod fastcgi \  
&& [ -d /var/cache/smokeping ] || mkdir -p /var/cache/smokeping \  
&& [ -d /var/lib/smokeping ] || mkdir -p /var/lib/smokeping \  
&& [ -d /run/smokeping ] || mkdir -p /run/smokeping \  
&& rmdir /var/www/cgi-bin \  
&& ln -s /usr/share/smokeping/www /var/www/smokeping \  
&& ln -s /usr/lib/cgi-bin /var/www/ \  
&& ln -s /usr/lib/cgi-bin/smokeping.cgi /var/www/smokeping/ \  
&& chown -Rh smokeping:www-data /var/cache/smokeping /var/lib/smokeping \  
/run/smokeping \  
&& chmod -R g+ws /var/cache/smokeping /var/lib/smokeping /run/smokeping \  
&& chmod u+s /usr/bin/fping \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
# lighttpd debug  
# && echo 'debug.log-request-handling = "enable"' >>$conf \  
# && echo 'debug.log-file-not-found = "enable"' >>$conf \  
COPY resources/Probes /etc/smokeping/config.d/  
COPY resources/Targets /etc/smokeping/config.d/  
COPY resources/docker-entrypoint.sh /usr/local/bin/  
ADD https://github.com/kreuzwerker/envplate/releases/download/v0.0.8/ep-linux
/usr/local/bin/ep  
  
RUN chmod +x /usr/local/bin/*  
  
VOLUME ["/etc/smokeping", "/etc/ssmtp", "/var/lib/smokeping",
"/var/cache/smokeping", "/var/run/smokeping"]  
  
EXPOSE 80  
ENV LOOKUPS="127.0.0.11:www.google.com 127.0.0.11:www.yahoo.fr" \  
FORKS="5" \  
STEP="100" \  
OFFSET="50%" \  
IP_VERSION="4" \  
MIN_INTERVAL="0.5" \  
PINGS="5" \  
PORT="53" \  
PROTOCOL="udp" \  
RECORD_TYPE="A" \  
REQUIRE_ANSWERS="0" \  
REQUIRE_NOERROR="0" \  
TIMEOUT="5"  
# container volumes should be destroyed when changing STEP  
ENTRYPOINT [ "/usr/local/bin/docker-entrypoint.sh" ]

