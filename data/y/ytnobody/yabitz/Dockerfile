FROM ruby:2.3  
MAINTAINER ytnobody <ytnobody@gmail.com>  
  
RUN apt-get update && apt-get install -y git gcc make g++ mysql-client
libsasl2-dev libldap2-dev  
WORKDIR /root  
RUN git clone git://github.com/livedoor/yabitz.git  
WORKDIR /root/yabitz  
RUN bundle install  
ADD lib/yabitz/plugin/config_instant.rb
/root/yabitz/lib/yabitz/plugin/config_instant.rb  
ADD lib/yabitz/plugin/instant_membersource.rb
/root/yabitz/lib/yabitz/plugin/instant_membersource.rb  
ADD scripts/instant/register_user.rb
/root/yabitz/scripts/instant/register_user.rb  
ADD run.sh run.sh  
RUN chmod +x run.sh  
ADD user_add user_add  
RUN chmod +x user_add  
  
EXPOSE 8080  
CMD "./run.sh"  

