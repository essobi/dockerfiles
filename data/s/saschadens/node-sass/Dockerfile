FROM node:slim  
  
RUN apt-get -qq update \  
&& apt-get install apt-utils \--assume-yes  
  
RUN apt-get install ruby-dev \--assume-yes \  
&& apt-get install lftp \--assume-yes \  
&& apt-get install rubygems \--assume-yes \  
&& gem update \--system \  
&& gem install sass  
  
RUN echo 'set ftp:ssl-allow false' > ~/.lftprc  
  

