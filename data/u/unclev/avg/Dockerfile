FROM ubuntu:xenial  
#FROM phusion/baseimage  
MAINTAINER Victor Kulichenko <onclev@gmail.com>  
RUN set -x \  
&& buildDeps='curl' \  
&& apt-get update -qq \  
&& apt-get install -yq $buildDeps libc6-i386 --no-install-recommends \  
&& echo "Install AVG..." \  
&& curl -Ls
http://download.avgfree.com/filedir/inst/avg2013flx-r3118-a6926.i386.deb >
/tmp/avg.deb \  
&& dpkg -i /tmp/avg.deb \  
&& echo "Clean up unnecessary files..." \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN set -x \  
&& avgcfgctl -w UpdateVir.sched.Task.Disabled=true \  
&& /etc/init.d/avgd restart && avgupdate  
COPY avg /bin/avg  
ADD http://www.eicar.org/download/eicar.com.txt /malware/EICAR  
WORKDIR /malware  
ENTRYPOINT ["/bin/avg"]  

