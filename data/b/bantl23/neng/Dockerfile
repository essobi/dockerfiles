FROM ubuntu:trusty  
  
RUN apt-get update && \  
apt-get install -y curl wget man-db software-properties-common && \  
add-apt-repository -y ppa:git-core/ppa && \  
add-apt-repository -y ppa:ubuntu-toolchain-r/test && \  
add-apt-repository -y ppa:george-edison55/cmake-3.x && \  
add-apt-repository -y ppa:brightbox/ruby-ng && \  
echo "deb http://www.rabbitmq.com/debian/ testing main" >>
/etc/apt/sources.list.d/rabbitmq.list && \  
wget https://www.rabbitmq.com/rabbitmq-signing-key-public.asc && \  
apt-key add rabbitmq-signing-key-public.asc && \  
rm rabbitmq-signing-key-public.asc && \  
apt-get update && \  
apt-get install -y \  
gcc-5 \  
g++-5 \  
gdb \  
dpkg-dev \  
make \  
git-core \  
cmake \  
ruby2.2 \  
python-pip \  
sqlite3 \  
libboost1.55-all-dev \  
libpython3-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
libhiredis-dev \  
zlib1g-dev \  
libyaml-dev \  
libcurl4-openssl-dev \  
libffi-dev \  
libreadline-dev \  
python-software-properties \  
redis-server \  
rabbitmq-server  
  
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 60 --slave
/usr/bin/g++ g++ /usr/bin/g++-5  
  
RUN gem install rspec net-ssh simplecov  
  
RUN useradd -m -G sudo docker  
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
CMD ["/bin/bash"]  

