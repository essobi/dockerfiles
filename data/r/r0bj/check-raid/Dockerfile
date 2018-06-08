FROM ubuntu:16.04  
  
WORKDIR /root  
RUN apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys C208ADDE26C2B797
\  
&& echo "deb http://downloads.linux.hpe.com/SDR/repo/mcp/ xenial/current non-
free" > /etc/apt/sources.list.d/proliant.sources.list \  
&& apt-get update \  
&& apt-get install -y \--no-install-recommends cciss-vol-status hpacucli git
build-essential ca-certificates \  
&& git clone https://github.com/jeremycole/parse-hp-acu \  
&& cd parse-hp-acu/Parse-HP-ACU/ \  
&& perl Makefile.PL \  
&& make \  
&& make install \  
&& rm -rf /root/parse-hp-acu \  
&& apt-get remove -y \--purge git build-essential ca-certificates \  
&& apt-get autoremove -y \--purge \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
COPY raid.pl /raid.pl  
RUN chmod +x /raid.pl  
  
CMD ["/raid.pl"]  

