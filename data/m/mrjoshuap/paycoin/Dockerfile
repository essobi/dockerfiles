#  
# docker-paycoin A Docker Container for hosting a Paycoin Wallet  
# Copyright (C) 2015 Joshua Preston  
#  
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# This program is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with this program. If not, see <http://www.gnu.org/licenses/>.  
#  
FROM ubuntu  
  
MAINTAINER mrjoshuap  
  
LABEL Description="This image is used to start a paycoin wallet"
Vendor="mrjoshuap" Version="v0.3.3.0"  
  
#TODO: Do this for atomic  
#ENV container docker  
#  
#LABEL INSTALL="/paycoind.sh install"  
#LABEL UNINSTALL="/paycoind.sh uninstall"  
#LABEL RUN="/paycoind.sh run"  
# perform updates  
RUN apt-get update -y \  
&& apt-get install -y curl unzip \  
&& apt-get clean \  
&& rm -rf /var/cache/apt/* /var/lib/apt/lists/*  
  
ENV PAYCOIN_VERSION=v0.3.3.0  
ENV PAYCOIN_USER=paycoin  
ENV PAYCOIN_HOME=/${PAYCOIN_USER}  
ENV PAYCOIN_DATADIR=${PAYCOIN_HOME}/data  
  
RUN curl -L -o /tmp/linux64.zip
https://github.com/PaycoinFoundation/paycoin/releases/download/${PAYCOIN_VERSION}/linux64.zip
\  
&& cd /usr/local/bin ; unzip /tmp/linux64.zip paycoind \  
&& rm /tmp/linux64.zip \  
&& useradd -s /bin/bash -m ${PAYCOIN_USER} \  
&& mkdir -p ${PAYCOIN_HOME}  
  
VOLUME ${PAYCOIN_HOME}  
  
RUN chown -R ${PAYCOIN_USER}:${PAYCOIN_USER} ${PAYCOIN_HOME} \  
&& chmod 700 ${PAYCOIN_HOME}  
  
COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh  
COPY ./paycoin.sh /usr/local/bin/paycoin  
  
EXPOSE 8998 8999 9901 9902 9903  
# Run it as the paycoin user defined in environment variable  
USER ${PAYCOIN_USER}  
  
# Default arguments, can be overriden  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
CMD ["start"]  

