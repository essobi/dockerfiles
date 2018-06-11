FROM correl/erlang:17.1  
MAINTAINER Nathaniel Waisbrot <waisbrot@whoop.com>  
  
#VOLUME /webhooks  
ADD . /webhooks  
WORKDIR /webhooks  
RUN rebar get-deps  
RUN rebar compile  
  
CMD erl -noinput -pa ebin -pa deps/*/ebin -eval
'application:ensure_all_started(webhooks).'  

