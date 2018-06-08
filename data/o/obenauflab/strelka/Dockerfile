# Copyright (c) 2018 Tobias Neumann.  
#  
#  
# You should have received a copy of the GNU Affero General Public License  
# along with this program. If not, see <http://www.gnu.org/licenses/>.  
  
FROM ubuntu:16.04  
  
MAINTAINER Tobias Neumann <tobias.neumann.at@gmail.com>  
  
ARG VERSION_ARG  
  
ENV
PATH="/strelka-2.9.3.centos6_x86_64/bin:/manta-1.4.0.centos6_x86_64/bin:${PATH}"  
  
# binutils is required to run opencl programs  
RUN buildDeps='wget bzip2 python' \  
&& set -x \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget --no-check-certificate
https://github.com/Illumina/strelka/releases/download/v2.9.3/strelka-2.9.3.centos6_x86_64.tar.bz2
\  
&& tar xvjf strelka-2.9.3.centos6_x86_64.tar.bz2 \  
&& wget --no-check-certificate
https://github.com/Illumina/manta/releases/download/v1.4.0/manta-1.4.0.centos6_x86_64.tar.bz2
\  
&& tar xvjf manta-1.4.0.centos6_x86_64.tar.bz2

