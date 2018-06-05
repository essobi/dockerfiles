FROM bernardolins/dev-base  
  
MAINTAINER bernardolins28@gmail.com  
  
ENV BOOST_VERSION 1.57.0  
ENV BOOST_VERSION_LINK 1_57_0  
  
#### installing boost  
RUN wget
http://downloads.sourceforge.net/project/boost/boost/$BOOST_VERSION/boost_$BOOST_VERSION_LINK.tar.gz
\  
&& tar -xvzf boost_$BOOST_VERSION_LINK.tar.gz \  
&& cd boost_$BOOST_VERSION_LINK \  
&& ./bootstrap.sh \  
&& ./b2 \  
&& ./b2 install  

