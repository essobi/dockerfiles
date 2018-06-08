FROM ubuntu:latest  
MAINTAINER George Lewis <schvin@schvin.net>  
  
# dependent on ENV definitions for DOMAIN and RELAY  
  
ENV REFRESHED_AT 2018-05-31  
RUN apt-get update --fix-missing -y && apt-get upgrade -y  
RUN apt-get install -y ssmtp mutt w3m gnupg procmail nvi  
  
RUN groupadd s-mail  
RUN useradd s-mail -g s-mail -d /home/s-mail  
RUN mkdir -p /home/s-mail  
RUN chown -R s-mail:s-mail /home/s-mail  
RUN ln -s /usr/lib/mutt/pgpewrap /usr/bin/pgpewrap  
  
#RUN perl -p -i -e 's/mailhub=.*/mailhub=$RELAY/' /etc/ssmtp/ssmtp.conf  
#RUN perl -p -i -e 's/^#rewriteDomain=.*/rewriteDomain=$DOMAIN/'
/etc/ssmtp/ssmtp.conf  
#RUN perl -p -i -e 's/^hostname=.*/hostname=$DOMAIN/' /etc/ssmtp/ssmtp.conf  
#RUN perl -p -i -e 's/^#(FromLineOverride=YES)/$1/' /etc/ssmtp/ssmtp.conf  
#ADD etc/ssmtp.conf /etc/ssmtp/ssmtp.conf  
  
ENV HOME /home/s-mail  
USER s-mail  
WORKDIR /home/s-mail  
  
CMD ["-f", "~/Mail/inbox"]  
ENTRYPOINT ["/usr/bin/mutt"]  

