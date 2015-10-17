pip install git+https://github.com/craftoid/twitterbot
pip install vapory
git clone https://github.com/POV-Ray/povray
pip install pillow
pip install numpy
pip install vapory
brew install autoconf
brew install automake
brew install boost
cd povray/unix
./prebuild.sh
cd ../
./configure COMPILED_BY="luis uip <luispedro28@hotmail.com>"
make
make install