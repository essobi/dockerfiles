#### QNIBTerminal image  
# inspired by https://github.com/larrycai/docker-openldap  
# it is based on
https://github.com/rackerlabs/dockerstack/blob/master/keystone/openldap/Dockerfile  
# also the files/more.ldif from
http://www.zytrax.com/books/ldap/ch14/#ldapsearch  
FROM qnib/u-consul:14.04  
# install slapd in noninteractive mode  
RUN apt-get update \  
&& apt-get install -y nmap \  
&& echo 'slapd/root_password password password' | debconf-set-selections \  
&& echo 'slapd/root_password_again password password' | debconf-set-selections
\  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y slapd ldap-utils \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD files /ldap  
  
RUN service slapd start ;\  
cd /ldap &&\  
ldapadd -Y EXTERNAL -H ldapi:/// -f back.ldif &&\  
ldapadd -Y EXTERNAL -H ldapi:/// -f sssvlv_load.ldif &&\  
ldapadd -Y EXTERNAL -H ldapi:/// -f sssvlv_config.ldif &&\  
ldapadd -x -D cn=admin,dc=qnib,dc=org -w password -c -f front.ldif &&\  
ldapadd -x -D cn=admin,dc=qnib,dc=org -w password -c -f more.ldif  
ADD etc/supervisord.d/slapd.ini /etc/supervisord.d/  
ADD etc/consul.d/slapd.json /etc/consul.d/  

