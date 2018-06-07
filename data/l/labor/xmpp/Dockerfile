FROM ubuntu:trusty  
  
MAINTAINER seu <seu@panopticon.re>  
  
RUN useradd -r -m -U -d /var/lib/ejabberd -s /usr/sbin/nologin ejabberd  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install \  
locales \  
curl \  
git-core \  
build-essential \  
automake \  
libssl-dev libssl1.0.0 \  
libyaml-dev libyaml-0-2 \  
zlib1g-dev zlib1g \  
libexpat-dev libexpat1 \  
python2.7 \  
python-jinja2 \  
ca-certificates \  
erlang-base erlang-snmp erlang-ssl erlang-ssh erlang-webtool \  
erlang-tools erlang-xmerl erlang-corba erlang-diameter erlang-eldap \  
erlang-eunit erlang-ic erlang-os-mon \  
erlang-parsetools erlang-percept erlang-typer erlang-src erlang-dev && \  
rm -rf /var/lib/apt/lists/* && \  
cd /tmp && \  
git clone https://github.com/processone/ejabberd.git --branch 15.04 --single-
branch --depth=1 && \  
cd ejabberd && chmod +x autogen.sh && ./autogen.sh && \  
./configure --enable-pgsql --disable-pam --enable-zlib && \  
make && make install && \  
chown -R ejabberd:ejabberd /var/lib/ejabberd /etc/ejabberd \  
&& apt-get remove -y curl git-core build-essential automake libssl-dev
libyaml-dev zlib1g-dev libexpat-dev erlang-dev && \  
apt-get clean  
  
VOLUME /var/lib/ejabberd  
EXPOSE 5222 5269  
  
COPY ejabberd.yml /etc/ejabberd/  
  
CMD ejabberdctl start && \  
tail -F /var/log/ejabberd/ejabberd.log  

