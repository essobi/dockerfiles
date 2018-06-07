FROM perl:5  
  
# libregexp-ipv6-perl is libnet-whois-ip-perl requirement  
# will be no more installed by hand when libnet-whois-ip-perl hits Stretch  
RUN apt-get update && apt-get \--yes --no-install-recommends install \  
libnet-ip-perl libnet-netmask-perl libnet-dns-perl libxml-writer-perl
libstring-random-perl \  
libregexp-ipv6-perl libhtml-parser-perl libwww-mechanize-perl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# libnet-whois-ip-perl is not available yet on Debian Jessie but in next
release Stretch  
# See https://packages.debian.org/libnet-whois-ip-perl &
https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=847619  
RUN wget http://deb.debian.org/debian/pool/main/libn/libnet-whois-ip-
perl/libnet-whois-ip-perl_1.19-2_all.deb \  
&& dpkg -i libnet-whois-ip-perl_1.19-2_all.deb  
  
RUN git clone https://github.com/fwaeytens/dnsenum.git /src/dnsenum/ \  
&& chmod +x /src/dnsenum/dnsenum.pl  
  
WORKDIR /src/dnsenum  
  
CMD /src/dnsenum/dnsenum.pl  

