# Copyright (c) 2018 Tobias Neumann.  
#  
#  
# You should have received a copy of the GNU Affero General Public License  
# along with this program. If not, see <http://www.gnu.org/licenses/>.  
FROM ubuntu:16.04  
MAINTAINER Tobias Neumann <tobias.neumann.at@gmail.com>  
ARG VERSION_ARG  
ENV PATH="/circos-0.69-6/bin:${PATH}"  
# binutils is required to run opencl programs  
RUN buildDeps='git wget gcc g++ libc6-dev make zlib1g-dev libncurses-dev perl
curl ca-certificates cpanminus libgd-gd2-perl python bedtools' \  
&& set -x \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& cpanm Clone Config::General Font::TTF::Font Math::Bezier Math::Round
Math::VecStat Params::Validate Readonly Regexp::Common SVG Set::IntSpan
Statistics::Basic Text::Format List::MoreUtils \  
&& wget http://circos.ca/distribution/circos-0.69-6.tgz \  
&& tar xvfz circos-0.69-6.tgz  

