FROM debian:latest  
RUN apt-get update \  
&& apt-get install -y \--no-install-recommends python wget time build-
essential \  
&& wget http://www.alasir.com/software/ramspeed/ramspeed-2.6.0.tar.gz \  
&& tar xzf ramspeed-2.6.0.tar.gz \  
&& cd ramspeed-2.6.0 \  
&& ./build.sh \  
&& cp ./ramspeed /usr/bin/ \  
&& cd / \  
&& rm -r ramspeed-2.6.0.tar.gz ramspeed-2.6.0 \  
&& apt-get remove -y build-essential \  
&& apt-get autoremove -y \  
&& apt-get autoclean  
  
WORKDIR /benchmark/  
ADD . /benchmark/  
CMD ./run-all.sh  

