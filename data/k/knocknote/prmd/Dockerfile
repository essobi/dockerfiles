FROM ruby:2.4.1  
MAINTAINER Knocknote<tech@knocknote.co.jp>  
  
RUN gem install specific_install \  
&& gem specific_install https://github.com/interagent/prmd.git master  
CMD ["tail", "-f", "/dev/null"]  

