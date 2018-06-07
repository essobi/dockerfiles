FROM ubuntu:14.04  
RUN apt-get update -qq && apt-get install -qy make g++ libpam0g-dev wget git
gcj-jre-headless gcj-jre libwxbase2.8-0 bwxgtk2.8-0  
  
RUN mkdir /pkg  
  
# install erlang R16B21  
RUN wget -q https://packages.erlang-solutions.com/debian/pool/esl-
erlang_16.b.2-1~ubuntu~precise_amd64.deb -P /pkg  
RUN dpkg -i /pkg/esl-erlang_16.b.2-1~ubuntu~precise_amd64.deb  
RUN wget -q http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb
-P /pkg  
RUN sudo dpkg -i /pkg/erlang-solutions_1.0_all.deb  
# RUN sudo apt-get install -qy erlang  
# download riak repository (from Github)  
RUN git clone https://github.com/basho/riak.git /root/riak  
  
# install riak  
RUN make -C /root/riak rel  
  
EXPOSE 8087 8098 2222 8069 8080  
ADD ./run.sh /run.sh  
ADD ./riak_conv/ /riak_conv/  
  
RUN apt-get install -qy curl software-properties-common && apt-add-repository
ppa:brightbox/ruby-ng && apt-get update && apt-get install -qy ruby2.2 && gem
install bundler  
RUN gem install sinatra sinatra-contrib  
  
CMD ["./run.sh"]  
#CMD tail -f /dev/null  

