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
libqt5core5a \  
libqt5gui5 \  
libqt5widgets5 \  
libqt5printsupport5 \  
libicu57 \  
libmpfr4 \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
ARG VERSION=2.1.7  
ARG FILE=MiniZincIDE-$VERSION-bundle-linux-x86_64  
  
RUN cd /tmp \  
&& curl -LOSs
https://github.com/MiniZinc/MiniZincIDE/releases/download/$VERSION/$FILE.tgz \  
&& tar -xzf $FILE.tgz \  
&& (cd $FILE \  
&& cp minizinc flatzinc fzn-* mzn* solns2* /usr/local/bin \  
&& cp -r share/minizinc /usr/local/share/ \  
) \  
&& rm -rf $FILE.tgz $FILE  
  
ENV MZN_STDLIB_DIR=/usr/local/share/minizinc/  

