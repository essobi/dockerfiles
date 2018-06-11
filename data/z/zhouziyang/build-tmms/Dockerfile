FROM zhouziyang/android-dev  
MAINTAINER Ziyang Zhou <ziyang.zhou1987@gmail.com>  
  
RUN apt-get -qq update  
RUN apt-get -qqy install curl wget make perl python ant  
  
RUN wget -nv -O /usr/local/bin/build_tmms \  
"https://raw.githubusercontent.com/zhouziyang/build-tmms/master/build_tmms.sh"  
RUN chmod 555 /usr/local/bin/build_tmms  

