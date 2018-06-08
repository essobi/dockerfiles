FROM erlang:20.1.2  
# derived from debian  
RUN set -ex; \  
useradd --create-home codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
WORKDIR /workspace  
  
# we need to use /workspace/erlang because /workspace is $HOME and rebar3
fails  
COPY rootfs/workspace /workspace  
# `chown -R codewarrior:codewarrior /workspace` doesn't seem to work  
RUN chown -R codewarrior:codewarrior /home/codewarrior  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior \  
REBAR_COLOR=none  
  
RUN set -ex; \  
cd erlang; \  
rebar3 eunit; \  
rm -rf src/*.erl test/*.erl _build/test;  

