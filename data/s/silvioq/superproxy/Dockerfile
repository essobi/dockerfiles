FROM silvioq/mod_perl:httpd  
  
ADD cpan.d/* /cpan.d/  
  
RUN set -x \  
&& ONLYPRELOAD=yes /usr/local/bin/httpd-foreground \  
&& rm /cpan.d/*  
  
ADD perl.conf /usr/local/apache2/conf/extra/perl.conf  
ADD htdocs/* /usr/local/apache2/htdocs/  
  

