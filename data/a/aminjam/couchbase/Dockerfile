FROM debian:stable  
MAINTAINER Amin Jams <aminjam@outlook.com>  
  
################## BEGIN INSTALLATION ######################  
RUN export DEBIAN_FRONTEND=noninteractive && \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install wget libssl1.0.0 python && \  
wget -q http://packages.couchbase.com/releases/3.0.1/couchbase-server-
community_3.0.1-debian7_amd64.deb -O couchbase-server-community.deb && \  
dpkg -i couchbase-server-community.deb && \  
rm couchbase-server-community.deb  
  
# Add configurations  
ENV PATH /opt/couchbase/bin:/opt/couchbase/bin/tools:$PATH  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
##################### INSTALLATION END #####################  
# Couchbase Ports 4369, 8091, 80(92-99), 11210, 21(100-199)  
# More on that http://docs.couchbase.com/couchbase-manual-2.0/#network-ports  
EXPOSE 4369 8080 8091 8092 11207 11208 11209 11210 11211 11212 11213 11214
11215 21100 21101 21102 21103 21104 21105 21106 21107 21108 21109 21110 21111
21112 21113 21114 21115 21116 21117 21118 21119 21120 21121 21122 21123 21124
21125 21126 21127 21128 21129 21130 21131 21132 21133 21134 21135 21136 21137
21138 21139 21140 21141 21142 21143 21144 21145 21146 21147 21148 21149 21150
21151 21152 21153 21154 21155 21156 21157 21158 21159 21160 21161 21162 21163
21164 21165 21166 21167 21168 21169 21170 21171 21172 21173 21174 21175 21176
21177 21178 21179 21180 21181 21182 21183 21184 21185 21186 21187 21188 21189
21190 21191 21192 21193 21194 21195 21196 21197 21198 21199  
WORKDIR /opt/couchbase  
ENTRYPOINT ["/run.sh"]  
CMD []  

