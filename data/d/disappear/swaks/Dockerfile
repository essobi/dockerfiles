FROM debian:stable  
  
RUN \  
apt-get update && apt-get install -y \  
perl-base \  
curl \  
libnet-ssleay-perl \  
libnet-dns-perl \  
libauthen-ntlm-perl \  
&& curl -SLk
http://www.jetmore.org/john/code/swaks/files/swaks-20170101.0/swaks -o swaks \  
&& chmod +x swaks \  
&& mv swaks /usr/bin  
  
ENTRYPOINT ["/usr/bin/swaks"]  

