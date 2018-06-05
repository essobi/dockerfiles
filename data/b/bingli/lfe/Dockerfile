FROM erlang:18  
MAINTAINER Bing Li <enst.bupt@gmail.com>  
  
WORKDIR /opt/erlang/  
ADD https://github.com/rvirding/lfe/archive/master.tar.gz
/opt/erlang/lfe.tar.gz  
RUN tar zxvf lfe.tar.gz  
RUN mv /opt/erlang/lfe-master /opt/erlang/lfe  
RUN cd /opt/erlang/lfe && make && make install  
  
WORKDIR /root  
  
#RUN curl -L -o ./lfetool https://raw.github.com/lfe/lfetool/stable/lfetool  
#RUN bash ./lfetool install  
#RUN rm -rf /root/lfetool  
#RUN lfetool -x  
CMD ["lfe"]  

