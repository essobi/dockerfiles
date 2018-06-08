FROM debian:jessie  
  
COPY requirements.txt /requirements.txt  
COPY apt.txt /apt.txt  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y \  
curl build-essential python-dev python-pip python-wheel \  
libssl-dev libffi-dev libgmp-dev  
  
RUN curl -sSLf https://apt.mopidy.com/mopidy.gpg | apt-key add \- \  
&& curl -sSLf https://apt.mopidy.com/jessie.list >
/etc/apt/sources.list.d/mopidy.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends -y \  
$(apt-cache search '^mopidy-.*' | sed -e 's/ .*$//' | egrep -v 'gpodder|doc')
\  
$(cat apt.txt) \  
&& rm -rf /var/cache/apt/  
  
USER mopidy  
  
EXPOSE 6600 6680  
  
CMD "mopidy"  

