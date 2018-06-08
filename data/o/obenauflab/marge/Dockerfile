# Copyright (c) 2018 Tobias Neumann.  
#  
#  
# You should have received a copy of the GNU Affero General Public License  
# along with this program. If not, see <http://www.gnu.org/licenses/>.  
  
FROM ubuntu:16.04  
  
MAINTAINER Tobias Neumann <tobias.neumann.at@gmail.com>  
  
ARG VERSION_ARG  
  
  
RUN runDeps='gcc g++ libc6-dev make zlib1g-dev python libhdf5-serial-dev
python-h5py python-pip python-dev git python-tables' \  
buildDeps='unzip wget' \  
&& set -x \  
&& apt-get update && apt-get install -y $buildDeps $runDeps --no-install-
recommends \  
&& pip install wheel setuptools argparse numpy scipy \  
&& pip install sklearn tables twobitreader \  
&& pip install MACS2 \  
&& (cd /usr/local/bin ; wget
http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/bedClip ; chmod ug+x
bedClip) \  
&& (cd /usr/local/bin ; wget
http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/bedGraphToBigWig ; chmod
ug+x bedGraphToBigWig) \  
&& (cd /usr/local/bin ; wget
http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/bigWigSummary ; chmod
ug+x bigWigSummary) \  
&& (cd /usr/local/bin ; wget
http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/bigWigAverageOverBed ;
chmod ug+x bigWigAverageOverBed) \  
&& wget http://cistrome.org/MARGE/src/Py2_MARGE.zip \  
&& unzip Py2_MARGE.zip \  
&& cd Py2_MARGE \  
&& python setup.py install \  
&& sed -i 's/\/path\/to/\/usr\/local\/bin/g' /usr/local/lib/python2.7/dist-
packages/marge-1.0-py2.7.egg/marge/config.json \  
&& sed -i 's/\/installed//g' /usr/local/lib/python2.7/dist-
packages/marge-1.0-py2.7.egg/marge/config.json \  
&& sed -i
's/\/usr\/local\/bin\/MARGE\/reference\/directory/\/data\/hg38_RP_reference\//g'
/usr/local/lib/python2.7/dist-packages/marge-1.0-py2.7.egg/marge/config.json \  
&& sed -i 's/"\\[hg38|hg19|mm10|mm9\\]"/"hg38"/g'
/usr/local/lib/python2.7/dist-packages/marge-1.0-py2.7.egg/marge/config.json \  
&& sed -i 's/\/usr\/local\/bin\/marge_testdata\///g'
/usr/local/lib/python2.7/dist-packages/marge-1.0-py2.7.egg/marge/config.json \  
&& sed -i 's/sample1 sample2 sample3 sample4//g'
/usr/local/lib/python2.7/dist-packages/marge-1.0-py2.7.egg/marge/config.json \  
&& sed -i 's/\\[Gene_Only|Gene_Response\\]/Gene_Only/g'
/usr/local/lib/python2.7/dist-packages/marge-1.0-py2.7.egg/marge/config.json \  
&& sed -i 's/\\[GeneSymbol|RefSeq\\]/GeneSymbol/g'
/usr/local/lib/python2.7/dist-packages/marge-1.0-py2.7.egg/marge/config.json \  
&& sed -i 's/\/usr\/local\/bin\/marge/\/usr\/local\/lib\/python2.7\/dist-
packages\/marge-1.0-py2.7.egg\/marge/g' /usr/local/lib/python2.7/dist-
packages/marge-1.0-py2.7.egg/marge/config.json \  
&& apt-get install -y python3 python3-pip python3-dev --no-install-recommends
\  
&& rm -rf /var/lib/apt/lists/* \  
&& pip3 install setuptools wheel \  
&& pip3 install snakemake \  
&& apt-get purge -y --auto-remove $buildDeps

