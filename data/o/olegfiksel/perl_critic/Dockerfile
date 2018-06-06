FROM perl:latest  
  
MAINTAINER Oleg Fiksel  
  
COPY critic_html /opt/critic_html  
RUN cpanm --installdeps /opt/critic_html && ln -s /opt/critic_html/critichtml
/usr/bin/critichtml && ln -s /opt/critic_html/critictext /usr/bin/critictext
&& ln -s /opt/critic_html/test_perlver /usr/bin/test_perlver && ln -s -f
/usr/local/bin/perl /usr/bin/perl && rm -rf ~/.cpanm  
  
WORKDIR /tmp/workspace  

