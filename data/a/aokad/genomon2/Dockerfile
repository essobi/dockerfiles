FROM aokad/genomon2:step3  
  
MAINTAINER aokad <aokad@hgc.jp>  
  
# python package  
RUN pip install Cython && \  
pip install pysam && \  
pip install numpy && \  
pip install scipy && \  
pip install primer3-py && \  
pip install pandas && \  
pip install pyVCF && \  
\  
cd /tools && \  
wget https://github.com/bunbun/ruffus/archive/v2.6.3.tar.gz && \  
tar xzvf v2.6.3.tar.gz && \  
rm -f v2.6.3.tar.gz && \  
cd ruffus-2.6.3 && \  
python setup.py install && \  
\  
cd /tools && \  
git clone https://github.com/ravenac95/PyYAML && \  
cd PyYAML && \  
python setup.py install && \  
\  
cd /tools && \  
wget -nc https://github.com/aokad/GenomonPipeline/archive/v2.5.3.zip && \  
unzip v2.5.3.zip && \  
rm -f v2.5.3.zip && \  
cd GenomonPipeline-2.5.3 && \  
python setup.py install && \  
\  
cd /tools && \  
wget -nc https://github.com/Genomon-Project/GenomonSV/archive/v0.4.2rc.zip &&
\  
unzip v0.4.2rc.zip && \  
rm -f v0.4.2rc.zip && \  
cd GenomonSV-0.4.2rc && \  
python setup.py install && \  
\  
cd /tools && \  
wget -nc https://github.com/friend1ws/sv_utils/archive/v0.4.2beta.zip && \  
unzip v0.4.2beta.zip && \  
rm -f v0.4.2beta.zip && \  
cd sv_utils-0.4.2beta && \  
python setup.py install && \  
\  
cd /tools && \  
wget -nc https://github.com/Genomon-
Project/GenomonMutationFilter/archive/v0.2.1.zip && \  
unzip v0.2.1.zip && \  
rm -f v0.2.1.zip && \  
cd GenomonMutationFilter-0.2.1 && \  
python setup.py install && \  
\  
cd /tools && \  
wget -nc https://github.com/Genomon-Project/EBFilter/archive/v0.2.1.zip && \  
unzip v0.2.1.zip && \  
rm -f v0.2.1.zip && \  
cd EBFilter-0.2.1 && \  
python setup.py install && \  
\  
cd /tools && \  
wget -nc https://github.com/Genomon-Project/GenomonFisher/archive/v0.2.0.zip
&& \  
unzip v0.2.0.zip && \  
rm -f v0.2.0.zip && \  
cd GenomonFisher-0.2.0 && \  
python setup.py install && \  
\  
cd /tools && \  
wget -nc https://github.com/Genomon-
Project/GenomonMutationAnnotator/archive/v0.1.0.zip && \  
unzip v0.1.0.zip && \  
rm -f v0.1.0.zip && \  
cd GenomonMutationAnnotator-0.1.0 && \  
python setup.py install && \  
\  
cd /tools && \  
wget -nc https://github.com/Genomon-Project/GenomonQC/archive/v2.0.2.zip && \  
unzip v2.0.2.zip && \  
rm -f v2.0.2.zip && \  
cd GenomonQC-2.0.2 && \  
python setup.py install && \  
\  
cd /tools && \  
wget -nc https://github.com/aokad/GenomonPostAnalysis/archive/v1.4.1.zip && \  
unzip v1.4.1.zip && \  
rm -f v1.4.1.zip && \  
cd GenomonPostAnalysis-1.4.1 && \  
python setup.py install && \  
\  
cd /tools && \  
wget -nc https://github.com/Genomon-Project/paplot/archive/v0.5.5.zip && \  
unzip v0.5.5.zip && \  
rm -f v0.5.5.zip && \  
cd paplot-0.5.5 && \  
python setup.py install && \  
\  
cd /tools && \  
wget -nc https://github.com/ken0-1n/mutation_util/archive/v0.5.0.zip && \  
unzip v0.5.0.zip && \  
rm -f v0.5.0.zip && \  
cd mutation_util-0.5.0 && \  
python setup.py install && \  
\  
cd /tools && \  
wget -nc https://github.com/ken0-1n/GenomonHotspotCall/archive/v0.1.0.zip && \  
unzip v0.1.0.zip && \  
rm -f v0.1.0.zip && \  
cd GenomonHotspotCall-0.1.0 && \  
python setup.py install && \  
\  
cd /tools && \  
wget -nc https://github.com/Genomon-Project/fusionfusion/archive/v0.3.0.zip &&
\  
unzip v0.3.0.zip && \  
rm -f v0.3.0.zip && \  
cd fusionfusion-0.3.0 && \  
python setup.py install && \  
\  
cd /tools && \  
wget -nc https://github.com/friend1ws/annot_utils/archive/v0.1.0.zip && \  
unzip v0.1.0.zip && \  
rm -f v0.1.0.zip && \  
cd annot_utils-0.1.0 && \  
python setup.py install && \  
cd resource && \  
bash prep_data.sh && \  
mv /tools/annot_utils-0.1.0/lib/annot_utils/data/hg19/*
/usr/local/lib/python2.7/site-packages/annot_utils/data/hg19/ && \  
mv /tools/annot_utils-0.1.0/lib/annot_utils/data/hg38/*
/usr/local/lib/python2.7/site-packages/annot_utils/data/hg38/ && \  
mv /tools/annot_utils-0.1.0/lib/annot_utils/data/mm10/*
/usr/local/lib/python2.7/site-packages/annot_utils/data/mm10/ && \  
\  
cd /tools && \  
wget -nc https://github.com/friend1ws/fusion_utils/archive/v0.2.0.zip && \  
unzip v0.2.0.zip && \  
rm -f v0.2.0.zip && \  
cd fusion_utils-0.2.0 && \  
python setup.py install && \  
\  
cd /tools && \  
wget -nc https://github.com/friend1ws/chimera_utils/archive/v0.3.0.zip && \  
unzip v0.3.0.zip && \  
rm -f v0.3.0.zip && \  
cd chimera_utils-0.3.0 && \  
python setup.py install && \  
\  
cd /tools && \  
wget -nc
https://github.com/friend1ws/intron_retention_utils/archive/v0.3.0.zip && \  
unzip v0.3.0.zip && \  
rm -f v0.3.0.zip && \  
cd intron_retention_utils-0.3.0 && \  
python setup.py install && \  
\  
cd /tools && \  
wget -nc https://github.com/Genomon-
Project/GenomonExpression/archive/v0.3.0.zip && \  
unzip v0.3.0.zip && \  
rm -f v0.3.0.zip && \  
cd GenomonExpression-0.3.0 && \  
python setup.py install && \  
\  
cd /tools && \  
wget https://github.com/Genomon-Project/genomon_Rscripts/archive/v0.1.3.zip &&
\  
unzip v0.1.3.zip && \  
rm -f v0.1.3.zip && \  
\  
cd /tools && \  
touch dummy && \  
echo "export LD_LIBRARY_PATH=/usr/local/lib" >> /root/.bashrc  
  
CMD ["/bin/bash"]  

