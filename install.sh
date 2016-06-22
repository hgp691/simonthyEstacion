#instalacion de archivos

#creacion de las carpetas en usb que guardan los datos
sudo mkdir /mnt/usb
sudo mount /dev/sda1/ /mnt/usb/
sudo mkdir /mnt/usb/simonthy/
sudo mkdir /mnt/usb/simonthy/config/
sudo mkdir /mnt/usb/simonthy/datos/
sudo mkdir /mnt/usb/simonthy/logs/

#instalar libreria DHT11
sudo apt-get install python-dev -y
cd /mnt/usb/ && sudo git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd /mnt/usb/Adafruit_Python_DHT && sudo python setup.py install

#copiar los archivos de inicio
sudo cp /etc/rc.local /etc/rc.local.bup
sudo rm /etc/rc.local
sudo cp conf/rc.local /etc/rc.local

sudo cp /etc/crontab /etc/crontab.bup
sudo rm /etc/crontab
sudo cp conf/crontab /etc/crontab

#copiar los archivos de configuracion
sudo cp /config/*.json /mnt/usb/simonthy/config/ -r

#instalar servidor web
sudo apt-get install apache2 -y
sudo apt-get install php5 -y

sudo mkdir /var/www/html/webservices
sudo cp webservices/* /var/www/html/webservices/
