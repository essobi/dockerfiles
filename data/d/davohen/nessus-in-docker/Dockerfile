FROM ubuntu:16.04  
MAINTAINER David Ormbakken Henriksen  
  
#update image and install wget for fetching stuff  
RUN apt-get update \  
&& apt-get install -y wget \  
&& rm -rf /var/lib/apt/lists/*  
  
#fetch session token+latest version number and then download  
RUN TOKEN="$(wget -q -O - --no-check-certificate \  
https://www.tenable.com/products/nessus/select-your-operating-system | \  
grep -Po 'timecheck" class="hidden">\K[^<]*')" \  
&& VER="$(wget -q -O - --no-check-certificate \  
https://www.tenable.com/plugins/os.json | \  
grep -Po '"version":"\K[^"]*')" \  
&& wget -O /tmp/nessus.deb \--no-check-certificate \  
"https://downloads.nessus.org/nessus3dl.php?file=Nessus-$VER-
ubuntu1110_amd64.deb&licence_accept=yes&t=$TOKEN"  
  
#install nessus and do some house cleaning  
RUN dpkg -i /tmp/nessus.deb \  
&& rm /tmp/nessus.deb \  
&& apt-get remove -y wget  
  
#define private port  
EXPOSE 8834  
  
#start nessus service upon container initialization  
ENTRYPOINT ["/opt/nessus/sbin/nessusd"]

