apt update
apt install -y zsh curl ufw
ufw allow 22
ufw allow 80
ufw allow 443
ufw default deny incoming
ufw default allow incoming
ufw default allow outgoing
ufw status verbose
ufw -f enable

apt install -y git supervisor nginx python3-pip mysql-server
pip3 install jinja2 flask gevent gunicorn pymysql flask-sqlalchemy Flask-Migrate

mysql -u root -pemean1010 -e "DELETE FROM mysql.user WHERE User='';"
mysql -u root -pemean1010 -e "DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');"
mysql -u root -pemean1010 -e "DROP DATABASE IF EXISTS test;"
mysql -u root -pemean1010 -e "DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%';"
# 设置密码并切换成密码验证
mysql -u root -pemean1010 -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'emean1010';"

rm -f /etc/nginx/sites-enabled/default
rm -f /etc/nginx/sites-available/default

cp /var/www/door/door.conf /etc/supervisor/conf.d/door.conf
cp /var/www/door/door.nginx /etc/nginx/sites-enabled/door
chmod -R o+rwx /var/www/door

# 初始化
cd /var/www/door
python3 reset.py

# 重启服务器
service supervisor restart
service nginx restart

echo 'succsss'
echo 'ip'
hostname -I