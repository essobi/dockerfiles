FROM apluslms/grading-base:2.0  
  
RUN apt-get update -qqy && DEBIAN_FRONTEND=noninteractive apt-get install -qqy
--no-install-recommends \  
-o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" \  
build-essential \  
python3 \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
RUN apt-get update -qqy && DEBIAN_FRONTEND=noninteractive apt-get install -qqy
--no-install-recommends \  
-o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" \  
python3-setuptools \  
unzip \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
ARG VERSION=4.6.0  
ARG FILE=z3-$VERSION-x64-debian-8.10  
  
RUN cd /tmp \  
&& curl -LOSs
https://github.com/Z3Prover/z3/releases/download/z3-$VERSION/$FILE.zip \  
&& unzip -qq -o $FILE.zip \  
&& cp $FILE/bin/z3 /usr/local/bin/z3 \  
&& cp $FILE/bin/libz3.so /usr/local/lib/libz3.so \  
&& cp -r $FILE/bin/python/z3 /usr/local/lib/python$(python3 -V|grep -o
'[0-9]\\.[0-9]')/dist-packages/ \  
&& ldconfig \  
&& rm -rf $FILE $FILE.zip  

