FROM darkpixel/request-tracker-docker-base:0.8.5  
LABEL maintainer="Aaron C. de Bruyn <aaron@heyaaron.com>"  
  
WORKDIR /opt/src  
RUN curl -sLS
"https://download.bestpractical.com/pub/rt/release/rt-4.4.2.tar.gz" | tar
--strip-components=1 -xvzf - \  
&& ./configure --enable-graphviz --enable-gd --with-db-type=Pg --with-db-
host=database \  
&& make testdeps && make install  
  
RUN PERL_MM_USE_DEFAULT=1 cpan install \  
RT::Extension::Announce \  
RT::Extension::Gravatar \  
RT::Extension::MergeUsers \  
RT::Extension::QuickUpdate \  
RT::Extension::RepeatTicket \  
RT::Extension::ResetPassword \  
#RT::Extension::REST2 \  
RT::Extension::TicketLocking \  
RT::Extension::BounceEmail \  
RT::Action::SetPriorityFromHeader \  
&& rm -rf /root/.cpan  
  
COPY RT_SiteConfig.pm /tmp/RT_SiteConfig.pm  
COPY msmtprc /tmp/msmtprc  
COPY fetchmailrc /tmp/fetchmailrc  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
COPY msmtp-sendmail.sh /usr/local/bin/msmtp-sendmail.sh  
  
WORKDIR /opt/rt4  
  
EXPOSE 80  
ENTRYPOINT ["/sbin/tini", "--", "/usr/local/bin/entrypoint.sh"]  

