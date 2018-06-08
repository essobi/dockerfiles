FROM ubuntu:latest  
LABEL maintainer="etix@l0cal.com" description="Monero blockchain node (with
GPG verified binary)"  
  
RUN apt-get update && apt-get install -y curl bzip2 git gnupg  
  
WORKDIR /root  
  
RUN git clone \--depth=1 https://github.com/monero-project/monero.git && \  
gpg --import monero/utils/gpg_keys/* && \  
curl https://getmonero.org/downloads/hashes.txt > hashes.txt && \  
gpg --verify hashes.txt && \  
cat hashes.txt| grep "monero-linux-x64-v" | awk -F", " '{$0=$1}1' > binary.txt
&& \  
cat hashes.txt| grep "monero-linux-x64-v" | awk -F", " '{$0=$2}1' > sha256.txt
&& \  
rm -r monero  
  
RUN curl https://downloads.getmonero.org/cli/`cat binary.txt` -O && \  
echo `cat sha256.txt` '' `cat binary.txt` | sha256sum -c - && \  
tar -xjvf *.tar.bz2 && \  
cp ./monero-v*/monerod . && \  
rm *.tar.bz2 && \  
rm -r monero-v*  
  
VOLUME /root/.bitmonero  
  
EXPOSE 18080 18081  
ENTRYPOINT ["./monerod"]  
CMD ["--restricted-rpc", "--rpc-bind-ip=0.0.0.0", "--confirm-external-bind", "
--non-interactive", "--fluffy-blocks"]  
  

